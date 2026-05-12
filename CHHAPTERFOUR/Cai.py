def cai_mixed_problems():
    print("Choose problem type: 1=Add, 2=Sub, 3=Mult, 4=Div, 5=Random")
    choice = int(input("Selection: "))
    
    n1, n2 = random.randint(0, 9), random.randint(0, 9)
    
    # Handle random choice
    op_type = choice if choice != 5 else random.randint(1, 4)
    
    if op_type == 1:
        question = f"{n1} + {n2}"
        correct = n1 + n2
    elif op_type == 2:
        question = f"{n1} - {n2}"
        correct = n1 - n2
    elif op_type == 3:
        question = f"{n1} * {n2}"
        correct = n1 * n2
    else: # Division
        if n2 == 0: n2 = 1 # Avoid division by zero
        question = f"{n1} / {n2}"
        correct = n1 // n2 # Using integer division for simplicity

    while True:
        ans = int(input(f"How much is {question}? "))
        if ans == correct:
            print("Very good!")
            break
        print("No. Try again.")
