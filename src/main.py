import re

from flask import Flask, request
from flask import render_template
from flask_wtf.csrf import CSRFProtect

from stop_words import STOP_WORDS
from settings_local import SECRET_KEY

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
    # TODO: Clean the message to avoid XSS attacks
    user_message = wrap_message(unparsed_message, is_bot=False)

    parsed_message = parse_message(unparsed_message)
    # TODO: Add a call to Wikimedia API to complete the answer
    bot_anwser = wrap_message(parsed_message, is_bot=True)

    context = {}
    # TODO: Keep more than one message in the history
    # make it scrollable and responsive.
    context["message_history"] = [user_message, bot_anwser]
    return render_template("messages.html", **context)


def parse_message(message: str) -> str:
    parsed_message = message
    parsed_message = parsed_message.lower()
    # Make a list with the words, excluding special characters
    # and numbers.
    splitted_message = re.split(r'[^a-zA-Z0-9À-ÿ]+', parsed_message)
    parsed_message = list(splitted_message)

    # Cleanse the list from stop words
    for word in splitted_message:
        for stop_word in STOP_WORDS:
            if word == stop_word:
                parsed_message.remove(word)
                break

    # Remove empty extra spaces if any
    parsed_message = " ".join(parsed_message).strip()

    return parsed_message


def wrap_message(message: str, is_bot: bool) -> str:
    """
    Wrap a message and format it depending on if this is
    the bot talking or the user.
    """
    formated_message = ""

    if is_bot:
        formated_message = "<b>GrandPy:</b> " + message
    else:
        formated_message = "<b>Vous:</b> " + message

    return formated_message
