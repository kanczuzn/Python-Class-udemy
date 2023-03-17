import requests as rq
from tkinter import messagebox
import datetime as dt
import json
import re

PIXELA_SITE = "https://pixe.la"
PIXELA_ENDPOINT = f"{PIXELA_SITE}/v1/users"
TODAY = dt.datetime.today()

# # Delete Graph
# def del_graph(username: str, graph_id: str):
#     header = {
#         "X-USER-TOKEN": get_token(username)
#     }
#     response = rq.delete(url=f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}", headers=header)
#     print(response)
#     print(response.text)

# # Delete User
# def del_user(username: str):
#     header = {
#         "X-USER-TOKEN": get_token(username)
#     }
#     response = rq.delete(url=f"{PIXELA_ENDPOINT}/{username}", headers=header)
#     print(response)
#     print(response.text)


# Create User
def new_user(username: str, token: str):
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = rq.post(url=PIXELA_ENDPOINT, json=user_params)
    if response.status_code == 200:
        with open(f"./usr_data/{username}.json", "w") as file:
            entry = {
                "username": username,
                "token": token,
                "graphs": [],
            }
            usr_dict = json.dumps(entry)
            file.write(usr_dict)

    return response.status_code, response.json()['message']


def graphs(username: str):
    response = rq.get(url=f"{PIXELA_SITE}/@{username}")
    user_graphs = re.findall(f'https://pixe\.la/v1/users/{username}/graphs/(.*)\.html', response.text)
    return user_graphs


def get_token(username: str):
    try:
        with open(f"./usr_data/{username}.json", "r") as file:
            data = json.load(file)
            token = data['token']
            return token
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="It looks like your user file is corrupted.")
        return


def create_graph(username: str, graph_id: str, graph_name: str, graph_unit: str, unit_type: str, graph_color: str):
    header = {
        "X-USER-TOKEN": get_token(username)
    }

    match graph_color:
        case "green":
            color = "shibafu"
        case "red":
            color = "momiji"
        case "blue":
            color = "sora"
        case "yellow":
            color = "ichou"
        case "purple":
            color = "ajisai"
        case "block":
            color = "kuro"
        case _:
            color = "shibafu"

    graph_config = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": unit_type,
        "color": color,
    }
    if len(header['X-USER-TOKEN']) > 0:
        graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
        response = rq.post(url=graph_endpoint, json=graph_config, headers=header)
        if response.status_code == 200:
            return response.status_code, f"{graph_name} successfully added!"
        else:
            return response.status_code, response.json()['message']


def find_datapoints(user: str, graph: str):
    find_datapoints_url = f'{PIXELA_ENDPOINT}/{user}/graphs/{graph}/pixels'
    header = {
        "X-USER-TOKEN": get_token(user)
    }
    response = rq.get(url=find_datapoints_url, headers=header)
    if response.status_code == 200:
        return response.status_code, response.json()['pixels']
    else:
        return response.status_code, response.json()['message']


def add_pixel(user: str, graphid: str, datapoint: str, quantity: str):
    # Posting a Pixel
    if datapoint == 'today':
        day = TODAY.strftime("%Y%m%d")
    else:
        day = convert_date(datapoint)
    posting_endpoint = f"{PIXELA_ENDPOINT}/{user}/graphs/{graphid}"
    header = {
        "X-USER-TOKEN": get_token(user)
    }

    pixel_config = {
        "date": day,
        "quantity": quantity,
    }
    response = rq.post(url=posting_endpoint, headers=header, json=pixel_config)
    return response.status_code, response.json()['message']


def get_units(user: str, graphid: str):
    posting_endpoint = f"{PIXELA_ENDPOINT}/{user}/graphs/{graphid}/graph-def"
    header = {
        "X-USER-TOKEN": get_token(user)
    }

    response = rq.get(url=posting_endpoint, headers=header)
    if response.status_code == 200:
        units_or_message = response.json()['unit']
        name = response.json()['name']
    else:
        units_or_message = response.json()['message']
        name = "Error"
    return response.status_code, units_or_message, name


def get_datapoint_value(user: str, graphid: str, datapoint: str):
    header = {
        "X-USER-TOKEN": get_token(user)
    }
    date = convert_date(datapoint)
    posting_endpoint = f"{PIXELA_ENDPOINT}/{user}/graphs/{graphid}/{date}"
    response = rq.get(url=posting_endpoint, headers=header)
    if response.status_code == 200:
        return response.status_code, response.json()['quantity']
    else:
        return response.status_code, response.json()['message']


def convert_date(date: str):
    converted_date = date.replace('/', '')
    converted_date = converted_date[4:] + converted_date[0:2] + converted_date[2:4]
    return converted_date
