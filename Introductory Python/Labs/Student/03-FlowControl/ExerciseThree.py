# Ask the user for a day, month, and year.
from datetime import timedelta, datetime
import calendar
day = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year (0 to 2099): "))
print("---------------------")

# Add the rest of your code here.

# If statement for leap year


def leapyear(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a leap year")


leapyear(year)
print("---------------------")


def dateformat(day, month, year):
    thirtydaymonth = [9, 4, 6, 11, 2]
    leapyear = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
    if day not in range(1, 32):
        print("Not a valid date")
    elif month in thirtydaymonth and day == 31:
        print("Not a valid date")
    elif day > 29 and month == 2:
        print("Not a valid date")
    elif not leapyear and day == 29:
        print("Not valid")
    elif year >= 2000 and year <= 2099:
        print("Year out of range")
    else:
        print(f"{day}/{month}/{year}")


dateformat(day, month, year)
print("---------------------")

day = timedelta(days=1)
date1 = datetime(year, month, 1)
d = date1
dates = []
while d.month == month:
    dates.append(d.strftime('%d/%m/%Y'))
    d += day
print(dates)
