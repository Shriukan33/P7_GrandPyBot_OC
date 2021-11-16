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
    context["message"] = """Perdu ? Demandez votre chemain à GrandPybot,
    le cyberpapy !"""
    return render_template("home.html", **context)


@app.route("/ajax/parser")
def parser(request):
    # TODO: Implement ajax parser
    return render_template("home.html")
