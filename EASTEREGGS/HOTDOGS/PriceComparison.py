first_weight = float(input("Enter weight of package 1: "))
first_packageprice = float(input("Enter price of package 1: "))

second_weight = float(input("Enter weight of package 2: "))
second_packageprice = float(input("Enter price of package 2: "))

first_price = first_packageprice / first_weight
second_price = second_packageprice / second_weight

if first_price < second_price:
    print("Package 1 has better price")
elif second_price < first_price:
    print("Package 2 has better price")
else:
    print("Both have same price")
