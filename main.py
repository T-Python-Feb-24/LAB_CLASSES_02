from bank_account import BankAccount

account = BankAccount("abdullah", 100)

print("Account holder:", account.get_account_holder())  
print("Initial balance:", account.get_balance())  

account.deposit(100)
print("Balance after deposit:", account.get_balance())
try:
    account.withdraw(300)
    print("Withdrawal successful. Remaining balance:", account.get_balance())
except ValueError as e:
    print(f"Withdrawal error:", str(e))

# Try to withdraw $200 (which exceeds the balance)
try:
    account.withdraw(50)
    print("Withdrawal successful. Remaining balance:", account.get_balance())
except ValueError as e:
    print(e)

# Get John's current balance
print("Current balance for", account.get_account_holder() + ":", account.get_balance())