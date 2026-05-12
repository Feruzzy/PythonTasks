import random

def play_guess_the_number():
    secret = random.randint(1, 1000)
    guesses = 0
    print("Guess my number between 1 and 1000:")
    
    while True:
        guess = int(input("Enter guess: "))
        guesses += 1
        if guess < secret:
            print("Too low. Try again.")
        elif guess > secret:
            print("Too high. Try again.")
        else:
            print("Congratulations. You guessed the number!")
            if guesses <= 10:
                print("Either you know the secret or you got lucky!")
            else:
                print("You should be able to do better!")
            break
