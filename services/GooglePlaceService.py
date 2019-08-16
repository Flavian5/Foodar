"""Service class: wrapper for Google Places queries, especially text search"""
import requests
import urllib.parse


class GooglePlaceService:
    string = "AIzaSyCoAfxtpSsCGFcR2WxQDCeWqO9BOFFr3xs"
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/jkey={}&son?query=".format(string)

    def search(self, query):
        full_url = self.base_url + urllib.parse.urlencode({"query": query})
        response = requests.get(url=full_url)
        return response.json()
