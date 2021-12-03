from src.wikimedia_api import WikiAPI


def test_get_page_info():
    """
    Test that we retrieve the page info

    For instance, we expect the wikipedia Page "Paris"
    to have the id 681159.
    """
    wiki = WikiAPI()
    assert wiki.get_page_info("Paris") is not None
    assert wiki.get_page_info(
        "Paris")["query"]["search"][0]["pageid"] == 681159


def test_get_page_id():
    """
    Tests that we can retrieve the page id of a page.
    """
    wiki = WikiAPI()
    assert wiki.get_page_id("Paris") == 681159
    assert wiki.get_page_id("Paris") is not None


def test_get_extract():
    """
    Tests that we can retrieve the short extract of a page.
    This extract is shown in grandpy's message.
    """
    wiki = WikiAPI()
    assert wiki.get_extract(681159) is not None
    assert wiki.get_extract(681159).startswith("Paris")


def mock_get_extract(page_id: int) -> str:
    """
    Mocks the get_extract method but only returns a string.
    The goal of this mock is to not make the test of
    get_wiki_answer fail if get_extract fails.

    We want to test the logic of get_wiki_answer, not get_extract's.
    Doing so, we avoid the get_wiki_answer to fail if get_extract fails.

    In my opinion, it is easier to pinpoint bugs if we test the logic
    rather than the integration.
    """
    return "valid"


def test_get_page_url():
    """
    Tests that we get the page URL corresponding to the ID.
    """
    wiki = WikiAPI()
    assert wiki.get_page_url(681159) is not None
    assert wiki.get_page_url(681159).startswith(
        "https://fr.wikipedia.org/wiki/Paris")


def mock_get_page_url(page_id: int) -> str:
    """
    This mocks the get_page_url method but only returns a string.
    The goal of this mock is to not make the test of
    get_wiki_answer fail if get_page_url fails.

    We want to test the logic of get_wiki_answer, not get_page_url's.
    Doing so, we avoid the get_wiki_answer to fail if get_page_url fails.
    """
    return "https://fr.wikipedia.org/wiki/Paris"


def test_get_wiki_answer():
    wiki = WikiAPI()
    # We mock the get_page_url method to return a string.
    # Doing so we avoid the test to fail if get_page_url fails
    # as we want to test get_wiki_answer's logic.
    wiki.get_page_url = mock_get_page_url
    # We mock the get_extract method to return a string.
    # Doing so we avoid the test to fail if get_page_url fails
    # as we want to test get_wiki_answer's logic.
    wiki.get_extract = mock_get_extract

    # In its execution, get_wiki_answer() will call the mock
    # functions get_page_url and get_extract.
    # Doing so, we avoid the test to fail if get_page_url or
    # get_extract fails as we want to test get_wiki_answer's logic.
    assert wiki.get_wiki_answer("Paris") is not None
    assert wiki.get_wiki_answer(
        "Paris")["url"] == wiki.get_page_url(681159)
    assert wiki.get_wiki_answer("Paris")["extract"] == wiki.get_extract(681159)
