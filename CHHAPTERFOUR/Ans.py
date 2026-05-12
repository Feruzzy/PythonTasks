def multiplication_tutor():
    n1, n2 = random.randint(0, 9), random.randint(0, 9)
    while True:
        ans = int(input(f"How much is {n1} times {n2}? "))
        if ans == n1 * n2:
            print("Very good!")
            break
        print("No. Please try again.")

