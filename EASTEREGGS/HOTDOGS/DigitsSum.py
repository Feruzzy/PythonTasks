number = int(input("Enter an integer (0–1000): "))
temp = number
total = 0

while temp > 0:
    total += temp % 10
    temp //= 10

print("Sum of digits:", total)
