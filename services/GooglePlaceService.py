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
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key={}&location={},{}&".format(
        string, latitude, longitude)
    photo_url = "https://maps.googleapis.com/maps/api/place/photo?"

    def search(self, query):
        full_url = self.base_url + urllib.parse.urlencode({"query": query})
        print(full_url)
        response = requests.get(url=full_url)
        print(response)
        print(response.content)
        return response.json()

    def get_photos(self, photo_reference):
        params = {"key": self.string, "photo_reference": photo_reference, "maxheight": 150}
        full_url = self.photo_url + urllib.parse.urlencode(params)
        response = requests.get(url=full_url)
        return response.json()
