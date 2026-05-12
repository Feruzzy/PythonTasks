def cai_difficulty():
    level = int(input("Enter difficulty level (1 or 2): "))
    max_val = 9 if level == 1 else 99
    n1, n2 = random.randint(0, max_val), random.randint(0, max_val)
    
    while True:
        ans = int(input(f"How much is {n1} times {n2}? "))
        if ans == n1 * n2:
            print("Very good!")
            break
        else:
            print("No. Please try again.")
