import requests


class WikiAPI:
    """
    This class groups the functions needed for the Wikimedia
    API to be used.
    Documentation is here:
    https://www.mediawiki.org/wiki/API:Main_page
    """

    def __init__(self):
        """
        This function initializes the class.
        """
        self.api_url = "https://fr.wikipedia.org/w/api.php"

    def get_page_info(self, query: str) -> dict:
        """
        This function gets the page info of the 1st hit of a
        search on the Wikipedia API.
        """
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "srlimit": 1
        }
        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_page_id(self, query: str) -> int:
        """
        This function gets the page id of the 1st hit of a
        search on the Wikipedia API.
        """
        page_info = self.get_page_info(query)
        if page_info is not None:
            return page_info["query"]["search"][0]["pageid"]
        else:
            return None

    def get_extract(self, page_id: int) -> str:
        """
        This function gets the 3 first sentences of a page.
        """
        params = {
            "action": "query",
            "format": "json",
            "formatversion": "latest",
            "prop": "extracts",
            "exsentences": 3,
            "explaintext": True,
            "pageids": page_id
        }
        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            extract = response.json()
            return extract["query"]["pages"][0]["extract"]
        else:
            return None

    def get_page_url(self, page_id: int) -> str:
        """
        This function gets the url of a page.
        """
        params = {
            "action": "query",
            "format": "json",
            "formatversion": "latest",
            "prop": "info",
            "inprop": "url",
            "pageids": page_id
        }
        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            url = response.json()
            return url["query"]["pages"][0]["fullurl"]
        else:
            return None

    def get_wiki_answer(self, query: str) -> dict:
        """
        This function gets the page info of the 1st hit of a
        search on the Wikipedia API and the 3 first sentences of
        the page.
        """
        try:
            page_id = self.get_page_id(query)
        except IndexError:
            return None

        if page_id is not None:
            extract = self.get_extract(page_id)
            url = self.get_page_url(page_id)
            return {
                "extract": extract,
                "url": url
            }
        else:
            return None
