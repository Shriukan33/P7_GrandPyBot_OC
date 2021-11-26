from src.message_handler import MessageHandler


def test_parse_message():
    mh = MessageHandler()
    assert mh.parse_message("Paris") == "paris"
    assert mh.parse_message(
        "<script>alert('alert!')</script>") == "script alert alert script"
    assert mh.parse_message("Bonjour, je m'appelle GRANDPY !") == "appelle"


def test_wrap_message():
    mh = MessageHandler()
    assert mh.wrap_message("Bonjour, je m'appelle BOT !", True) == \
        "<span class='bot_message'>GrandPy:</span> Bonjour, je m'appelle BOT !"
    assert mh.wrap_message("Bonjour, je m'appelle LUC !", False) == \
        "<span class='user_message'>Vous:</span> Bonjour, je m'appelle LUC !"


def test_add_wiki_answer():
    mh = MessageHandler()
    assert mh.add_wiki_answer(
        "Bonjour, ",
        {"url": "\'https://fr.wikipedia.org/wiki/Paris\'",
         "extract": "Paris est la capitale de la France"}) == \
        "Bonjour, Paris est la capitale de la France " + \
        "[<a href='https://fr.wikipedia.org/wiki/Paris'>En savoir" + \
        " plus sur Wikipedia</a>]"

    assert mh.add_wiki_answer("", None) == \
        "Peux tu répéter ? Mon audition n'est plus ce qu'elle était ..."


def test_add_address():
    mh = MessageHandler()
    assert mh.add_address(
        "Bonjour, ",
        "4 Pl. de l'Hôtel de Ville, 75004 Paris, France") == \
        "Bonjour, 4 Pl. de l'Hôtel de Ville, 75004 Paris, France. "

    assert mh.add_address("", None) == ""
