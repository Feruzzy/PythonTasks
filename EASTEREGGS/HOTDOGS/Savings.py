monthly_saving = float(input("Enter monthly saving amount: "))
monthly_rate = 0.003125

balance = 0

for number in range(1, 7):
    balance = (balance + monthly_saving) * (1 + monthly_rate)
    print(f"Month {number} balance: {balance:.2f}")
