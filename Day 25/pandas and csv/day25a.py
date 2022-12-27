# def main():
#     with open("weather_data.csv") as data_file:
#         data = data_file.readlines()
#     print(data)

# import csv
#
# def main():
#     temperatures = []
#     with open("weather_data.csv") as data_file:
#         data = csv.reader(data_file)
#         for row in data:
#             try:
#                 temperatures.append(int(row[1]))
#             except:
#                 pass
#     print(temperatures)

import pandas


def main():
    data = pandas.read_csv("weather_data.csv")
    print(data['temp'])

    data_dict = data.to_dict()
    print(data_dict)

    temp_list = data['temp'].to_list()
    print(temp_list)

    print(data['temp'].mean())
    print(data['temp'].max())
    data.temp.mean()
    print(data.condition)

    # Get Data in Row
    print(data[data.day == "Monday"])
    print(data[data.temp == data.temp.max()])

    monday = data[data.day == "Monday"]
    print(monday.condition)
    monday_temp = int(monday.temp)
    monday_temp = monday_temp * (9/5) + 32
    print((9/5)*monday.temp+32)
    print(monday_temp)

    # Create Dataframe
    data_dict = {
        "students": ["Amy", "James", "Angela",],
        "scores": [76, 56, 65, ]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("new_data.csv")


if __name__ == "__main__":
    main()
