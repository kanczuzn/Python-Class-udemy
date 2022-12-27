import pandas


def main():
    fur_color = []
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    data_fur = data['Primary Fur Color'].drop_duplicates().dropna()
    for fur in data_fur:
        fur_color.append(fur)
    squirrel_dict = {
        "Fur Color": fur_color,
        "Count": [0] * len(fur_color),
    }
    for fur in range(len(fur_color)):
        squirrel_dict['Count'][fur] = data['Primary Fur Color'].value_counts()[fur_color[fur]]
    squirrel_count = pandas.DataFrame(squirrel_dict)
    squirrel_count.to_csv("squirrel_data.csv")

if __name__ == "__main__":
    main()