pin = int(input("Enter a 4-digit PIN: "))

if pin >= 1000 and pin <= 9999:
    print("Valid PIN")
else:
    print("Invalid PIN")

