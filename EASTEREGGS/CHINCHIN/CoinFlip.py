import random

coin = random.randint(0, 1) 
guess = int(input("Enter 0 for head or 1 for tail: "))

if guess == coin:
    print("Your guess is correct!")
else:
    print("Your guess is incorrect.")

print("The actual result was:", coin)
print()
