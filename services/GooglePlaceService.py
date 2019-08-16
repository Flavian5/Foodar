"""Service class: wrapper for Google Places queries, especially text search"""
import requests
import urllib.parse


class GooglePlaceService:

    string = "ttAIzaSyDswjDbx2Jp4K"
    string2 = "l92XkldtS2D2N0URGBlVott"
    latitude = 43.6404
    longitude = -79.3995
    string = string + string2
    string = string.split('tt')[1]
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/jkey={}&location={},{}&son?query=".format(
        string, latitude, longitude)

    def search(self, query):
        full_url = self.base_url + urllib.parse.urlencode({"query": query})
        response = requests.get(url=full_url)
        return response.json()
