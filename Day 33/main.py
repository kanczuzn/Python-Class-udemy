import requests
from datetime import datetime
import time


def main():
    try:
        curr_lat = float(input("What's your latitude? "))
        curr_long = float(input("What's your latitude? "))
    except ValueError:
        print("Please input a valid value.")
    else:
        parameters = {
            "lat": curr_lat,
            "long": curr_long,
            "formatted": 0,
        }
        iss_loc(parameters)


def iss_loc(parameters):
    response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    iss_track = True

    while iss_track:
        time_now = datetime.now().hour
        if time_now < sunrise or time_now > sunset:
            info = requests.get(url="http://api.open-notify.org/iss-now.json")
            if info.status_code != 200:
                info.raise_for_status()
            else:
                location = (
                    float(info.json()['iss_position']['latitude']),
                    float(info.json()['iss_position']['longitude'])
                )
                print(f"Location: {location}\n")
                if abs(location[0] - parameters['lat']) <= 5 and \
                        abs(location[1] - parameters['long']) <= 5:
                    print("Look up!")
        else:
            pass
        time.sleep(60)


if __name__ == "__main__":
    main()
