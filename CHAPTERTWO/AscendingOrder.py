first_number = float(input("Enter first number: ")
second_number = float(input("Enter second number: ")
third_number = float(input("Enter third number: ")

if first_number <= second_number and first_number <= third_number:
    if second_number <= third_number:
        print(first_number, second_number, third_number)
    else:
        print(first_number, third_number, second_number)

elif second_number <= first_number and second_number <= third_number:
    if first_number <= third_number:
        print(second_number, first_number, third_number)
    else:
        print(second_number, third_number, first_number)

else:
    if first_number <= second_number:
        print(third_number, first_number, second_number)
    else:
        print(third_number, second_number, first_number)
    


