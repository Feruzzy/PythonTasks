import random

def get_response(is_correct):
    if is_correct:
        responses = ['Very good!', 'Nice work!', 'Keep up the good work!']
    else:
        responses = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']
    return random.choice(responses)

def cai_fatigue_reduction():
    n1, n2 = random.randint(0, 9), random.randint(0, 9)
    while True:
        ans = int(input(f"How much is {n1} times {n2}? "))
        if ans == n1 * n2:
            print(get_response(True))
            break
        else:
            print(get_response(False))

