def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print(f"{'Celsius':>10} {'Fahrenheit':>12}")
for c in range(101):
    print(f"{c:10d} {fahrenheit(c):12.1f}")

