# An extra day is added to the calendar almost every four years as February 29,
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. 


def is_leap(year):
    leap = False
    # Write your logic here
    if not year%4:
        if not year%100:
            if not year%400:
                leap=True
            else:
                return leap
        else:
            leap=True
    else:
        return leap
    
    return leap


year= int(input("Enter year : "))

print(is_leap(year))