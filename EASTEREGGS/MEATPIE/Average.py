total = 0

number_counter = 0

number = int(input("Enter integer: "))


for number in range(3):

    total += number
    number_counter += 1
    number = int(input("Enter integer: "))


average = total / 3

    

print(f'Class average is {average}')
