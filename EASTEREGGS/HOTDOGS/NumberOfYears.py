minutes = int(input("Enter number of minutes: "))


days = minutes // (60 * 24)
years = days // 365
remaining_days = days % 365


print("Years:", years)
print("Days:", remaining_days)
