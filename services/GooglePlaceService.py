"""Service class: wrapper for Google Places queries, especially text search"""
import requests
import urllib.parse


class GooglePlaceService:
    string = "AIzaSyCoAfxtpSsCGFcR2WxQDCeWqO9BOFFr3xs"
    latitude = 43.6404
    longitude = -79.3995
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/jkey={}&location={},{}&son?query=".format(
        string, latitude, longitude)

    def search(self, query):
        full_url = self.base_url + urllib.parse.urlencode({"query": query})
        response = requests.get(url=full_url)
        return response.json()
