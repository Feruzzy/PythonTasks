total = 0

miles_gallons = 0


gallons = float(input("Enter the gallons used, end if -1: "))
miles = float(input("Enter the miles driven, end if -1: "))

result = miles / gallons



while gallons != -1:
    total += result
    miles_gallons += 1
    gallons = float(input("Enter the gallons used, end if -1: "))
miles = float(input("Enter the miles driven, end if -1: "))
result = miles / gallons

   


if miles_gallons != 0:
    average = total / miles_gallons

    print(f'The average of the grades is {average:.2f}')

else:
    print("No grade was entered")
