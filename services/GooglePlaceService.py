"""Service class: wrapper for Google Places queries, especially text search"""
import requests
import urllib.parse
import shutil
from google.cloud import storage
from settings import *

class GooglePlaceService:

    latitude = 43.6404
    longitude = -79.3995

    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key={}&location={},{}&".format(
        API_KEY, latitude, longitude)
    photo_url = "https://maps.googleapis.com/maps/api/place/photo?"
    client_id = 'YOUR CLIENT ID'
    client_secret = 'YOUR CLIENT SECRET'

    def search(self, query):
        full_url = self.base_url + urllib.parse.urlencode({"query": query})
        print(full_url)
        response = requests.get(url=full_url)
        print(response)
        print(response.content)
        return response.json()

    def get_photos(self, name, photo_reference):
        params = {"key": API_KEY, "photo_reference": photo_reference, "maxheight": 150}
        full_url = self.photo_url + urllib.parse.urlencode(params)
        response = requests.get(url=full_url, stream=True)
        with open('{}.png'.format(name), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        storage_client = storage.Client()
        bucket_name = 'foodar'
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob('{}.png'.format(name))
        blob.upload_from_filename('{}.png'.format(name))
        return blob.generate_signed_url()
