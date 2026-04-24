number = int(input("Enter a two-digit integer: "))

tens = number // 10
units = number % 10

if tens > units:
    print("The tens digit is greater than the units digit.")
elif tens < units:
    print("The tens digit is less than the units digit.")
else:
    print("The tens digit is equal to the units digit.")

print()
