speed = float(input("Enter speed in km/h: "))

if speed == 0:
    print("Stationary")
elif speed >= 1 and speed <= 40:
    print("Slow")
elif speed >= 41 and speed <= 80:
    print("Moderate")
elif speed >= 81 and speed <= 120:
    print("Fast")
else:
    print("Dangerously Fast")
print()
