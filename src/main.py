
from bleach import clean
from flask import Flask, request
from flask import render_template
from flask_wtf.csrf import CSRFProtect

from settings_local import SECRET_KEY

from message_handler import MessageHandler as mh
from wikimedia_api import wikiAPI as wiki


app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = SECRET_KEY


@app.route("/")
def landing_page():
    context = {}
    context["message_history"] = []
    return render_template("home.html", **context)


@app.route("/ajax/parser", methods=['GET', 'POST'])
def parser():
    data = request.form.to_dict()

    unparsed_message = data["unparsed_message"]

    parsed_message = mh.parse_message(unparsed_message)

    # TODO: Add call to Google maps API here

    wiki_answer = wiki()
    wiki_answer = wiki.get_wiki_answer(wiki_answer, parsed_message)
    if wiki_answer:
        bot_message = f"{parsed_message}, wiki dit : {wiki_answer['extract']}"
    else:
        bot_message = "Pardon, tu peux répéter ? Mon audition n'est plus" + \
            " ce qu'elle était ..."

    bot_anwser = mh.wrap_message(bot_message, is_bot=True)

    # Cleanse the message to avoid malicious code
    cleaned_message = clean(unparsed_message, strip=True)
    user_message = mh.wrap_message(cleaned_message, is_bot=False)

    context = {}
    # TODO: Keep more than one message in the history
    # make it scrollable and responsive.
    context["message_history"] = [user_message, bot_anwser]
    return render_template("messages.html", **context)
