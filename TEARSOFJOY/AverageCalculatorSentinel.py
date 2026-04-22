total = 0
count = 0

while True:
    number = int(input("Enter your number: "))
    if number == -1:
        break
    total += number
    count += 1

if count > 0:
    print("Count:", count, "Average:", total / count)
else:
    print("No numbers entered")
