rate = float(input("Enter exchange rate (USD to RMB): "))
choice = int(input("Enter 0 for USD→RMB or 1 for RMB→USD: "))

if choice == 0:
    usd = float(input("Enter USD: "))
    print("RMB:", usd * rate)
elif choice == 1:
    rmb = float(input("Enter RMB: "))
    print("USD:", rmb / rate)
else:
    print("Invalid input")
