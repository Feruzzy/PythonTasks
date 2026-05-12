def move_tortoise(pos):
    i = random.randint(1, 10)
    if 1 <= i <= 5: pos += 3   # Fast plod
    elif 6 <= i <= 7: pos -= 6 # Slip
    else: pos += 1             # Slow plod
    return max(1, pos)

def move_hare(pos):
    i = random.randint(1, 10)
    if 1 <= i <= 2: pass       # Sleep
    elif 3 <= i <= 4: pos += 9 # Big hop
    elif i == 5: pos -= 12     # Big slip
    elif 6 <= i <= 8: pos += 1 # Small hop
    else: pos -= 2             # Small slip
    return max(1, pos)

def race():
    t, h = 1, 1
    print("BANG !!!!!\nAND THEY'RE OFF !!!!!")
    while t < 70 and h < 70:
        t, h = move_tortoise(t), move_hare(h)
        track = [" "] * 71
        if t == h: track[t] = "OUCH!!!"
        else:
            if t < 71: track[t] = "T"
            if h < 71: track[h] = "H"
        print("".join(track[1:]))
    
    if t >= 70 and h >= 70: print("IT'S A TIE.")
    elif t >= 70: print("TORTOISE WINS!!! YAY!!!")
    else: print("Hare wins. Yuch.")

