import requests

from src.maps_api import MapsAPI


def mock_get_lat_lng_request_does_404(address: str) -> None:
    """
    Mock for get_lat_lng() that returns None when the request returns a 404

    The request is modified so it always 404 for further test purposes.
    """
    maps = MapsAPI()
    maps.params["address"] = address
    # Mock a 404 response
    response = requests.get("https://google.com")
    response.status_code = 404
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            lat = data["results"][0]["geometry"]["location"]["lat"]
            lng = data["results"][0]["geometry"]["location"]["lng"]
            coordinates = {"lat": lat, "lng": lng}
            return coordinates
    else:
        return None


def test_get_lat_lng():
    """"
    Tests successively the get_lat_lng() function with a valid address and
    a 404 response.
    """
    maps = MapsAPI()
    assert maps.get_lat_lng("Paris") is not None
    assert maps.get_lat_lng("Paris")["lat"] == 48.856614
    assert maps.get_lat_lng("Paris")["lng"] == 2.3522219
    # The original get_lat_lng() function is replaced by a mock function
    # that has a failing request (404)
    maps.get_lat_lng = mock_get_lat_lng_request_does_404
    assert maps.get_lat_lng("Paris") is None


def mock_get_address_request_does_404(lat: float, lng: float) -> None:
    """
    Mock of get_address() that returns None when the request returns a 404

    The request is modified so it always 404 for further test purposes.
    """
    maps = MapsAPI()
    params = maps.params
    params["latlng"] = f'{lat},{lng}'
    if params["address"]:
        del params["address"]
    # Mock a 404 response
    response = requests.get("https://google.com")
    response.status_code = 404
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            address = data["results"][0]["formatted_address"]
            return address
    else:
        return None


def test_get_address():
    """
    Tests successively the get_address() function with a valid lat and lng and
    a 404 response.
    """
    maps = MapsAPI()
    assert maps.get_address(48.856614, 2.3522219) is not None
    assert maps.get_address(48.856614, 2.3522219) == \
        "4 Pl. de l'Hôtel de Ville, 75004 Paris, France"
    # The original get_address() function is replaced by a mock function
    # that has a failing request (404)
    maps.get_address = mock_get_address_request_does_404
    assert maps.get_address(48.856614, 2.3522219) is None
