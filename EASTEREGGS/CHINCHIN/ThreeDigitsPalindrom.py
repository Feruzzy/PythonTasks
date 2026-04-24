palindrom_number = int(input("Enter a 3-digit integer: "))


first_digit = p_num // 100
last_digit = p_num % 10

if first_digit == last_digit:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

print()
