from src.wikimedia_api import WikiAPI


def test_get_page_info():
    wiki = WikiAPI()
    assert wiki.get_page_info("Paris") is not None
    assert wiki.get_page_info(
        "Paris")["query"]["search"][0]["pageid"] == 681159


def test_get_page_id():
    wiki = WikiAPI()
    assert wiki.get_page_id("Paris") == 681159
    assert wiki.get_page_id("Paris") is not None


def test_get_extract():
    wiki = WikiAPI()
    assert wiki.get_extract(681159) is not None
    assert wiki.get_extract(681159).startswith("Paris")


def mock_get_extract(page_id: int) -> str:
    return "valid"


def test_get_page_url():
    wiki = WikiAPI()
    assert wiki.get_page_url(681159) is not None
    assert wiki.get_page_url(681159).startswith(
        "https://fr.wikipedia.org/wiki/Paris")


def mock_get_page_url(page_id: int) -> str:
    return "https://fr.wikipedia.org/wiki/Paris"


def test_get_wiki_answer():
    wiki = WikiAPI()
    wiki.get_page_url = mock_get_page_url
    wiki.get_extract = mock_get_extract
    assert wiki.get_wiki_answer("Paris") is not None
    assert wiki.get_wiki_answer(
        "Paris")["url"] == wiki.get_page_url(681159)
    assert wiki.get_wiki_answer("Paris")["extract"] == wiki.get_extract(681159)
