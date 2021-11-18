
from bleach import clean
from flask import Flask, request
from flask import render_template
from flask_wtf.csrf import CSRFProtect

from settings_local import SECRET_KEY

from message_handler import MessageHandler as mh

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
    # Cleanse the message to avoid malicious code
    cleaned_message = clean(unparsed_message, strip=True)
    user_message = mh.wrap_message(cleaned_message, is_bot=False)

    parsed_message = mh.parse_message(unparsed_message)
    # TODO: Add a call to Wikimedia API to complete the answer
    bot_anwser = mh.wrap_message(parsed_message, is_bot=True)

    context = {}
    # TODO: Keep more than one message in the history
    # make it scrollable and responsive.
    context["message_history"] = [user_message, bot_anwser]
    return render_template("messages.html", **context)
