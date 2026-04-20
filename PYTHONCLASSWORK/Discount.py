"""
Tells user to input amount spent
if amount spent is greater greater than 1000 and less than or equal to 10000 store it in first discount
print amount minus first discount

elif amount spent is greater than 10000 and less than or equal to 50000 store it in first discount
print amount minus second discount

elif amount spent is greater or equal to 50000 store it in first discount
print amount minus third discount
"""











amount_spent = int (input("Enter the amount spent: "))





if amount_spent >=1000  and amount_spent <= 10000:
    first_discount = ((5 * amount_spent) / 100)
    print(amount_spent - first_discount)


elif amount_spent >=10000  and amount_spent <= 50000:
    second_discount = ((10 * amount_spent) / 100)
    print(amount_spent - second_discount)

else:
    third_discount = ((10 * amount_spent) / 100)
    print(amount_spent - third_discount)


  




