import json
import requests


def get_api(address):
    response = requests.get(address)
    if response.status_code == 200:
        return json.loads(response.text)
