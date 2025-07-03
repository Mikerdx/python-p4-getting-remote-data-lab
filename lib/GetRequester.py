# GetRequester.py
import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # This returns raw bytes (matches JSON_STRING)

    def load_json(self):
        response = requests.get(self.url)
        return response.json()  # This parses JSON and returns a Python list
