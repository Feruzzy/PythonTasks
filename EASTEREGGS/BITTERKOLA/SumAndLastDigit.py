number = int(input("Enter a 5-digit integer: "))

first_digit = number // 10000
last_digit = number % 10

total = first_digit + last_digit
print("Sum of first and last digits:", total)
print()
