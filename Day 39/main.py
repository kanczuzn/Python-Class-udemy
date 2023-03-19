from data_manager import DataManager
from flight_search import FlightSearch

ORIGIN_CITY = "San Diego"


def main():
    data_manager = DataManager()
    sheet_info = data_manager.get_sheet_data()
    flight_search = FlightSearch()

    update = False

    for destination in sheet_info:
        if destination['iataCode'] == "":
            update = True
            destination['iataCode'] = flight_search.get_iata_code(destination['city'])

    if update:
        data_manager.destination_data = sheet_info
        data_manager.update_sheet_data()

    for destination in data_manager.destination_data:
        flight = flight_search.get_flights(ORIGIN_CITY, destination['iataCode'])
        try:
            if flight.price < destination["lowestPrice"]:
                print(f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to"
                      f" {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} "
                      f"to {flight.return_date}."
                      )
        except AttributeError:
            print("No flight found.")


if __name__ == "__main__":
    main()
