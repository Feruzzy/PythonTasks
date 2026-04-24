investment = float(input("Enter investment amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

monthly_rate = annual_rate / 1200
future_value = investment * (1 + monthly_rate) ** (years * 12)

print("Future investment value:", future_value)
