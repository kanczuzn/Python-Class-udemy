from os import environ
import requests as rq

SHEETY_URL = environ.get('ENV_SHEETLY_URL')
SHEETY_AUTH = f"Bearer {environ.get('ENV_SHEETLY_AUTH')}"
SHEETY_HEADER = {
    "Authorization": SHEETY_AUTH
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_sheet_data(self):
        response = rq.get(url=SHEETY_URL, headers=SHEETY_HEADER)
        response.raise_for_status()
        self.destination_data = response.json()['prices']
        return self.destination_data

    def update_sheet_data(self):
        for destination in self.destination_data:
            new_info = {
                "price": {
                    "iataCode": destination['iataCode']
                }
            }
            url = f"{SHEETY_URL}/{destination['id']}"
            response = rq.put(url=url, headers=SHEETY_HEADER, json=new_info)
            response.raise_for_status()
