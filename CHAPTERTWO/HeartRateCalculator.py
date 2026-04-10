age = int(input("Enter your age: ")

MaxHeartRate = 220 - age

lower = MaxHeartRate * 0.50
higher = MaxHeartRate * 0.85

print("Maximum Heart Rate:", MaxHeartRate)
print("Target Heart Rate Ranger", int(lower), "to", int(upper))

