birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year
print("Age:", age)

if age >= 65:
    print("Eligible for senior citizen discount.")
else:
    print("Not eligible for senior citizen discount.")
print()
