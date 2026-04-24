number = int(input("Enter a 4-digit integer: "))


fourth_digit = number % 10          
third_digit = (number // 10) % 10  
second_digit = (number // 100) % 10 
first_digit = number // 1000       

print("Reversed:", fourth_digit, third_digit, second_digit, first_digit, sep="")

print()
