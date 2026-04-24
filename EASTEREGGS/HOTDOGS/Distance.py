u = float(input("Enter initial velocity (u): "))
t = float(input("Enter time (t): "))
a = float(input("Enter acceleration (a): "))

s = u * t + 0.5 * a * t**2
print("Distance covered:", s)
