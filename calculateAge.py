import time
from calendar import isleap

#judge the leap year
def judge_leap_year(year):


    if year % 4 == 0:
        return True
    else:
        return False

#returns the number of days in each month
def month_days(month, leap_year):


    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

name = input("Enter your name: ")
age = input("Enter your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

#calculate the days
for y in range(begin_year,end_year):
    if judge_leap_year(y):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range (1, localtime.tm_mon):
    day = day + month_days(m, leap_year)
    # days_in_month = month_days(m, leap_year)  # Store the result in a variable
    # if days_in_month is not None:  # Check if it's not None
    #     day += days_in_month
    # else:
    #     # Handle the case where month_days returns None (optional)
    #     print(f"Warning: Days for month {m} could not be determined")

day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end = "")
print("%d months or %d days" % (month, day))
#
