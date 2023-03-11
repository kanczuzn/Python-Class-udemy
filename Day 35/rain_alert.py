import requests as rq

# Based on openweathermap api
api_key = ""
location = ""
OWM_endpoint = ""
exclude = "current,minutely,daily"
lat = 0
long = 0
parameters = {
    "lat": lat,
    "lon": long,
    "exclude": exclude,
    "appid": api_key,
}


data = rq.get(OWM_endpoint, params=parameters)
data.raise_for_status()
weather = data.json()["hourly"][0:13]

will_rain = False
for hourly in weather:
    if 200 <= hourly["weather"][0]["id"] <= 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")
