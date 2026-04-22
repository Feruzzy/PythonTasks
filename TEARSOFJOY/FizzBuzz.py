for number in range(1, 51):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", end=" ")

    elif number % 3 == 0:
        print("Fizz", end=" ")

    elif number % 5 == 0:
        print("Buzz", end=" ")

    else:
        print(number, end=" ")
print()
