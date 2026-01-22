import requests
import json 
import logging


def get_data():
    url="https://api.openbrewerydb.org/v1/breweries/"

    response = requests.get(url)

    try:
        with open('data.json', 'w+') as f:
            json.dump(response.json(), f)
    except:
        logging.exception("message")

get_data()