principal = float(input("Task 27 - Enter Principal: "))
rate = float(input("Task 27 - Enter Rate (in %): "))
time = float(input("Task 27 - Enter Time (years): "))

# Convert rate to decimal
rate_dec = rate / 100


simple_interest = principal * rate_dec * time


compound_interest = principal * (1 + rate_dec)**time - principal

print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
