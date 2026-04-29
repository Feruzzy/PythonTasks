def largest_number(first_number, second_number, third_number):
    largest_number = first_number
    if largest_number < second_number:
        largest_number = second_number
    if second_number < third_number:
        largest_number = third_number
    return largest_number

print(largest_number(1000, 4000, 5))
