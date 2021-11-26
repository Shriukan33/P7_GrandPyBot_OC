import requests

from .settings_local import MAPS_API_KEY


class MapsAPI:
    """
    This class holds all the functions related to Google API.
    """

    def __init__(self):
        self.key = MAPS_API_KEY
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.params = {
            "key": self.key,
            "region": "fr",
            "address": "",
        }

    def get_lat_lng(self, address):
        """
        This function returns the latitude and longitude of an address.
        """
        self.params["address"] = address
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                lat = data["results"][0]["geometry"]["location"]["lat"]
                lng = data["results"][0]["geometry"]["location"]["lng"]
                coordinates = {"lat": lat, "lng": lng}
                return coordinates
        else:
            return None

    def get_address(self, lat, lng):
        """
        This function returns the address of a latitude and longitude.
        """
        params = self.params
        params["latlng"] = f"{lat},{lng}"
        if params["address"]:
            del params["address"]
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                address = data["results"][0]["formatted_address"]
                return address
        else:
            return None
