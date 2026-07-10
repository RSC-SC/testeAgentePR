import requests
import json

def fetch_data(url):
    response = requests.get(url)
    return json.loads(response.text)