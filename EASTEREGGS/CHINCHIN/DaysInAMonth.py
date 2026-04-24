month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif month == 2:
    # Basic leap year check
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
else:
    days = 0

print("Number of days in month:", days)
print()
