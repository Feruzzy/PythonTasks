"""
This function calculates the sum of the squares of all elements in the input list.
For [1, 2, 3, 4, 5], the result is 1 + 4 + 9 + 16 + 25 = 55.
"""

def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y

