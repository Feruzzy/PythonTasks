import random

first_number = random.randint(0, 9)
second_number = random.randint(0, 9)

print("Positive Difference")
print("First number:", first_number)
print("Second number:", second_number)

# To keep the result positive, we always subtract the small one from the big one
if first_number > second_number:
    result = first_number - second_number
else:
    result = second_number - first_number

print("The difference is:", result)
print()
