from ui import PixelaInterface
from os import listdir


def main():
    user = "New User"
    for file in listdir("./usr_data"):
        if file.endswith(".json"):
            user = file.split('.json')[0]

    PixelaInterface(user)


if __name__ == "__main__":
    main()
