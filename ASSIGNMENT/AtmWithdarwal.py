"""
What ATM need as input
-card: To know the account i want to withdraw from and which bank i belong to.

Pin: My personal password to prove i own the card.

Amount: The amount of cash i want to withdraw.

Account choice: Whether the money comes from my savings or current.

Decision it makes
- Is this the right person: it compares the PIN i typed with the one stored in the banks record.
- Is there sufficient money in the account: it asks the bank computer if my account balance is higher than the amount i ask for.
- Is there enough money in the ATM: it checks if it has enough physical #500 or #1000 bills inside.
- Am i allowed to take this much: it checks if i have already hit my daily limit.


ATM ALGORITHM

1. Identify: i put my card in the ATM reads my name and account number.

2. Verify: i type my PIN if it is wrong three times the ATM stops me for safety

3. Request: i ask for a specific amount of money.

4. Checks: The ATM calls my bank. The bank says yes or no based on my balance.

5. Count: if the bank says the ATM counts out the bills.

6. Deliver: The ATM pushes my cash out then ask if i want to do another transaction
- if yes it repeats 2.
- if no it gives me my card.

7. Record: It prints a receipt showing how much i took and how much is left.

POSSIBLE REULTS(OUTPUTS)
- Success: i get my cash and a receipt.
- Denial: A message saying Insufficient Funds or Daily Limit Reached.
-Security Lock: The ATM keeps my card if it thinks its stolen or if i forgot i PIN too many times.
-Empty ATM: A message saying out of service if it has run out of cash.
"""
