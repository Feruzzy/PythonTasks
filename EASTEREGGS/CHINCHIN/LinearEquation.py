a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("The equation has no unique solution.")
else:
    
    x = (c - b) / a
    print("The solution x is:", x)

print()
