

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month!"
    if year < 0:
        return "Invalid year!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = is_leap(year)
    month = month - 1
    if leap_year is True and month == 1:
        return month_days[month] + 1
    else:
        return month_days[month]


# 🚨 Do NOT change any of the code below
def main():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)


if __name__ == "__main__":
    main()
