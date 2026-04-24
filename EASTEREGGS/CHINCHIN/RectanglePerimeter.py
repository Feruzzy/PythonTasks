first_edge = float(input("Enter length of edge 1: "))
second_edge = float(input("Enter length of edge 2: "))

if first_edge != second_edge:
    perimeter = 2 * (first_edge + second_edge)
    print("The perimeter is:", perimeter)
else:
    print("Input is invalid (edges must be different lengths).")

print()
