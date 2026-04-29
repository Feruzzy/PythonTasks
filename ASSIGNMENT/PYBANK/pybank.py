def validate_email(email):
    if len(email) < 8:
        return False

    if "@" not in email or email.startswith("@") or email.endswith("@"):
        return False
    return True

def calculate_balance(transactions):
    return sum(transactions) if transactions else 0

def is_strong_password(password):
    return len(password) >= 8

def apply_interest(balance, rate, years):
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    if years < 1:
        raise ValueError("Years must be at least 1")
   
    final_balance = balance * ((1 + rate) ** years)
    return round(final_balance, 2)

def get_transaction_summary(transactions):
    total_credits = 0
    total_debits = 0
   
    for type_label, amount in transactions:
        if type_label == "credit":
            total_credits += amount
        elif type_label == "debit":
            total_debits += amount
           
    net_balance = total_credits - total_debits
    transaction_count = len(transactions)
   
    return [
        ["total_credits", total_credits],
        ["total_debits", total_debits],
        ["net_balance", net_balance],
        ["transaction_count", transaction_count]
    ]
