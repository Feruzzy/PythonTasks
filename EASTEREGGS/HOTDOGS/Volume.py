lenght = int(input("Enter the length of the sides of the Triangle: "))

square_of_lenght = lenght ** 2


multiplier = (3 / 4) ** 0.5

area = multiplier * square_of_lenght

volume = area * lenght
print("The volume of the Triangle is: ", volume,"cm3") 
