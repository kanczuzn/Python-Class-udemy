import requests as rq
import datetime as dt
from os import environ

GENDER = environ.get('ENV_GENDER')
WEIGHT_KG = environ.get('ENV_WEIGHT_KG')
HEIGHT_CM = environ.get('ENV_HEIGHT_CM')
AGE = environ.get('ENV_AGE')
APP_ID = environ.get('ENV_APP_ID')
APP_KEY = environ.get('ENV_APP_KEY')
SHEETLY_KEY = environ.get('ENV_SHEETLY_KEY')
SHEETLY_URL = environ.get('ENV_SHEETLY_URL')


def nutritionix():
    nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

    what_i_did = input("Tell me what exercises you did: ")

    header = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
    }

    exercise = {
        "query": what_i_did,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }

    response = rq.post(url=nutritionix_url, headers=header, json=exercise)
    response.raise_for_status()
    result = response.json()['exercises']
    for activity in result:
        sheetly(activity['name'], activity['duration_min'], activity['nf_calories'])


def sheetly(exercise: str, duration: int, calories: int):
    sheetly_url = environ.get(SHEETLY_URL)
    today = dt.datetime.now()
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%X")

    header = {
        "Authorization": f'Bearer {SHEETLY_KEY}'
    }

    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    response = rq.post(url=sheetly_url, json=body, headers=header)
    response.raise_for_status()


def main():
    nutritionix()


if __name__ == "__main__":
    main()
