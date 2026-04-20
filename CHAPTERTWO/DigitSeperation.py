num = int(input("Enter a five digit integer: ")


first_digit = num // 10000
second_digit = (num % 10000) // 1000
third_digit = (num % 1000) // 100
fourth_digit = (num % 100) // 10
fifth_digit = num % 10

print(first_digit, " ", second_digit, " ", third_digit, " ", fourth_digit, " ", fifth_digit)
