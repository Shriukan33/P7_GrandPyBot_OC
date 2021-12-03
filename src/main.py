import os

from bleach import clean
from flask import Flask, request, jsonify
from flask import render_template
from flask_wtf.csrf import CSRFProtect

from .message_handler import MessageHandler as mh
from .wikimedia_api import WikiAPI as wiki
from .maps_api import MapsAPI as maps


app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', "mysecret")


@app.route("/")
def landing_page():
    context = {}
    context["message_history"] = []
    context["maps_api_key"] = os.environ.get('MAPS_API_KEY', "")
    return render_template("home.html", **context)


@app.route("/ajax/parser", methods=['GET', 'POST'])
def parser():
    # At this point, data holds the CSRF token and the user's message
    data = request.form.to_dict()
    context = {}

    unparsed_message = data["unparsed_message"]

    # We parse the message to feed it to the apis.
    parsed_message = mh.parse_message(mh(), unparsed_message)

    # We use google's geocoding o the message to get the coordinates.
    coordinates = maps.get_lat_lng(maps(), parsed_message)
    if coordinates:
        latitude = coordinates["lat"]
        longitude = coordinates["lng"]
        formatted_address = maps.get_address(maps(), latitude, longitude)
    else:
        formatted_address = None

    # Perform a wikipedia search on the message.
    wiki_answer = wiki()
    wiki_answer = wiki.get_wiki_answer(wiki_answer, parsed_message)

    # Construction of the bot's message.
    bot_anwser = ""
    bot_anwser = mh.add_address(mh(), bot_anwser, formatted_address)
    bot_anwser = mh.add_wiki_answer(mh(), bot_anwser, wiki_answer)
    bot_anwser = mh.wrap_message(mh(), bot_anwser, is_bot=True)

    # Cleanse the message to avoid malicious code
    cleaned_message = clean(unparsed_message, strip=True)
    user_message = mh.wrap_message(mh(), cleaned_message, is_bot=False)

    # The two messages are going to be displayed in the central area.
    context["message_history"] = [user_message, bot_anwser]

    # myanswer is retrieved by Ajax and will update both messages and the map.
    myanswer = {}
    myanswer["message_history"] = render_template("messages.html", **context)
    myanswer["coordinates"] = coordinates

    return jsonify(myanswer)
