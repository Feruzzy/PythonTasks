distance = float(input("Enter distance to drive: "))
miles = float(input("Enter miles per gallon: "))
price = float(input("Enter price per gallon: "))

cost = (distance / miles) * price
print("Trip cost:", cost)
