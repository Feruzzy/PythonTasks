a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

if a > 0 and b > 0:
    print("Both positive. Sum:", a + b)
elif a < 0 and b < 0:
    print("Both negative. Product:", a * b)
else:
    # Opposite signs: Difference (Larger - Smaller)
    if a > b:
        print("Opposite signs. Difference:", a - b)
    else:
        print("Opposite signs. Difference:", b - a)
print()

