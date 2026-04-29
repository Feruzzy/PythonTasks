import pybank

def main():
transactions = []
    print("--- Welcome to PyBank App ---")
   
    
while True:
email = input("Enter email to login: ")
password = input("Enter your password my friend: ")
if pybank.validate_email(email) and pybank.is_strong_password(password):
    print("Login Successful!\n")
    break
    print("Invalid email or weak password. Try again.")

while True:
    print("\nMENU:")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Balance")
    print("4. View Summary")
    print("5. Project Compound Interest")
    print("6. Exit")
       
    choice = input("Select an option: ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        transactions.append(["credit", amount])
        print("Deposit recorded.")
       
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        transactions.append(["debit", amount])
        print("Withdrawal recorded.")

    elif choice == '3':
        simple_list = [amt if t == "credit" else -amt for t, amount in transactions]
        balance = pybank.calculate_balance(simple_list)
        print(f"Current Balance: ${balance}")

    elif choice == '4':
        summary = pybank.get_transaction_summary(transactions)
        for label, value in summary:
        print(f"{label.replace('_', ' ').title()}: {value}")

    elif choice == '5':
        try:
            simple_list = [amount if t == "credit" else -amount for t, amount in transactions]
            balance = pybank.calculate_balance(simple_list)
               
            rate = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))
            years = int(input("Enter number of years: "))
               
            future_val = pybank.apply_interest(balance, rate, years)
            print(f"Projected balance after {years} years: ${future_val}")
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
