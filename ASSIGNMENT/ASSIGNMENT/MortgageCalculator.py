principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate: "))
duration = float(input("Enter the duration in years: "))


r = (interest_rate / 100) / 12

n = (duration * 12)

sum = float(1 + r)
first_result = float(sum ** n)
second_result = first_result * r

#third_result = principal_amount * second_result


third_result = first_result - 1

fourth_result = second_result / third_result


monthly_payment = principal_amount * fourth_result



#monthly_payment = third_result / fourth_result


print("Your monthly payment is:", monthly_payment)
