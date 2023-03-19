import requests as rq
from os import environ
import datetime as dt
from dateutil.relativedelta import relativedelta
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API = environ.get('ENV_TEQUILA_API')


class FlightSearch:

    def __init__(self):
        self.header = {
            'apikey': TEQUILA_API
        }

    def get_iata_code(self, city_name):
        location_endpoint = f'{TEQUILA_ENDPOINT}/locations/query'
        query = {
            'term': city_name,
            'locale': 'en-US',
            'location_types': 'city',
        }
        response = rq.get(url=location_endpoint, headers=self.header, params=query)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code

    def get_flights(self, origin, city):
        location_endpoint = f'{TEQUILA_ENDPOINT}/search'
        query = {
            "fly_from": self.get_iata_code(origin),
            "fly_to": city,
            "date_from": str(dt.date.today() + dt.timedelta(days=1)),
            "date_to": str(dt.date.today() + relativedelta(months=+6)),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "USD",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = rq.get(url=location_endpoint, headers=self.header, params=query)
        response.raise_for_status()
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {city}.")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][-1:][0]['cityTo'],
            destination_airport=data['route'][1]['flyTo'],
            out_date=dt.datetime.fromtimestamp(data['route'][0]["dTime"]).date().strftime("%m/%d/%Y"),
            return_date=dt.datetime.fromtimestamp(data['route'][1]["dTime"]).date().strftime("%m/%d/%Y")
        )
        print(f'{origin} -> {city}: {flight_data.price}')
        print(f'{flight_data.destination_city}: {flight_data.price}')
        return flight_data
