# program to display calender
import calendar


def display_calendar(y, m):
    print(calendar.month(y, m))

    print(calendar.Month)


y = int(input("Enter year: "))
m = int(input("Enter month: "))

display_calendar(y, m)
