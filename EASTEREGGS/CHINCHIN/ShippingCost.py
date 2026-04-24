weight = float(input("Enter package weight: "))

if weight <= 0:
    print("Invalid weight.")
elif weight <= 2:
    print("Shipping cost: $2.5")
elif weight <= 4:
    print("Shipping cost: $4.5")
elif weight <= 10:
    print("Shipping cost: $7.5")
elif weight <= 20:
    print("Shipping cost: $10.5")
else:
    print("The package cannot be shipped.")

print()
