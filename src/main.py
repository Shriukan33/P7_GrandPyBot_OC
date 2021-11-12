from flask import Flask
from flask import render_template

from stop_words import STOP_WORDS

app = Flask(__name__)


@app.route("/")
def landing_page():
    context = {}
    context["message"] = """Perdu ? Demandez votre chemain à GrandPybot,
    le cyberpapy !"""
    return render_template("home.html", **context)


@app.route("/ajax/parser")
def parser(request):
    # TODO: Implement ajax parser
    return render_template("home.html")
