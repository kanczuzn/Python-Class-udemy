import smtplib
import datetime as dt
from random import choice
from custom_choice import usr_choice
import pandas as pd

# Mail address goes below. Needs e-mail, password, and SMTP
MY_EMAIL = ""
PASSWORD = ""
MY_SMTP = ""


def main():
    prog_start = True

    while prog_start:
        option = int(usr_choice("\nWhat would you like to do?\n"
                                "1 - Add/Remove a birthday?\n"
                                "2 - Check for birthdays?\n"
                                "3 - Exit Program\n\n"
                                "Choose option between 1 and 3: ", "1 2 3"))
        if option == 1:
            add_birthday()
        if option == 2:
            mail_out()
        if option == 3:
            prog_start = False


def add_birthday():
    try:
        birthdays = pd.read_csv('./birthdays.csv')

    except FileNotFoundError:
        print('No birthday.csv found.')

    else:
        add_rem_choice = usr_choice("\nWould you like to add or remove a birthday?(add/rem) ", "add rem")
        if add_rem_choice == "rem":
            rem_day = True
            while rem_day:
                print(birthdays)
                rem_day = usr_choice("\nWhich entry would you like to remove?(-1 to cancel) ", "#num# +-")
                if rem_day == -1:
                    rem_day = False
                else:
                    try:
                        birthdays = birthdays.drop(rem_day, axis="index")
                        birthdays.to_csv('./birthdays.csv', index=False)
                        rem_day = False
                    except KeyError:
                        print("That entry doesn't exist. Please try again, or type -1 to cancel.")

        if add_rem_choice == "add":
            add_day = True
            while add_day:
                name = input("\nWhat is their name? ").strip()
                email = input("What is their email? ").strip()
                print("\nPlease enter the birthday you wish to add.\n")
                year = int(usr_choice("Enter a year? ", "#num# +"))
                month = int(usr_choice("Enter a month? (1-12) ", "1 2 3 4 5 6 7 8 9 10 11 12"))
                day = int(usr_choice("Enter the day? ", "#num# +"))
                correct = usr_choice(f"\nName: {name}\n"
                                     f"E-mail: {email}\n"
                                     f"Birthdate (m/d/y): {month}/{day}/{year}\n\n"
                                     f"Is this information correct?(y/n) ", "y n")

                if correct == "y":
                    add_day = False
                    new_entry = pd.DataFrame([[name, email, year, month, day]], columns=birthdays.columns)
                    birthdays = pd.concat([birthdays, new_entry])
                    birthdays.to_csv('./birthdays.csv', index=False)

                if correct == "n":
                    stay = usr_choice("\nDo you still wish to add a birthday?(y/n) ", "y n")
                    if stay == "n":
                        add_day = False


def mail_out():
    name = input("What is the name of the sender? ").strip()
    try:
        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        with open("./letter_templates/" + choice(letters), "r") as file:
            letter = file.read()

    except FileNotFoundError:
        print("The letter was not found within the letter_templates folder..")

    else:
        curr_day = int(dt.datetime.now().day)
        curr_month = int(dt.datetime.now().month)
        try:
            birthdays = pd.read_csv('./birthdays.csv')
        except FileNotFoundError:
            print("No birthdays.csv found.")
        else:
            for entry in range(0, len(birthdays.index)):
                day = int(birthdays.iloc[entry]['day'])
                month = int(birthdays.iloc[entry]['month'])
                if curr_day == day and curr_month == month:
                    letter = letter.replace("[NAME]", birthdays.iloc[entry]['name'])
                    letter = letter.replace("Angela", name)
                    print(f"\nTo: {birthdays.iloc[entry]['email']}")
                    print(letter)
                    send_choice = usr_choice("\nDo you want to send the letter?(y/n) ", "y n")
                    if send_choice == "y":
                        their_email = birthdays.iloc[entry]['email']
                        with smtplib.SMTP(MY_SMTP) as connection:
                            connection.starttls()
                            connection.login(user=MY_EMAIL, password=PASSWORD)
                            connection.sendmail(
                                from_addr=MY_EMAIL,
                                to_addrs=their_email,
                                msg=f"Subject:Happy Birthday!\n\n{letter}"
                            )


if __name__ == "__main__":
    main()
