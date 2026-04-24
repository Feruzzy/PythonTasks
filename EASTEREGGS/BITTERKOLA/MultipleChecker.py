first_number = int(input("Enter first integer: "))
second_number = int(input("Enter second integer: "))

if first_number % second_number == 0:
    print(first_number, "is a multiple of", second_number)
else:
    print(first_number, "is not a multiple of", second_number)
print()
