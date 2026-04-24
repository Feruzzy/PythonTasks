monthly_salary = float(input("Enter monthly salary: "))
annual_salary = monthly_salary * 12
tax = 0

if annual_salary <= 300000:
    tax = 0
elif annual_salary <= 600000:
    tax = (annual_salary - 300000) * 0.15
else:
    tax = (300000 * 0.15) + (annual_salary - 600000) * 0.25

print("Annual tax owed: N", tax)
print()
