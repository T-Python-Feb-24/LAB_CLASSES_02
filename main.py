from BankAccount import BankAccount
account1 = BankAccount("Mohammed")
print("Name:", account1.get_account_holder(), "the current balance", account1.get_balance())

try:
    account1.deposit(2000)
    print("Name:", account1.get_account_holder(), "the current balance", account1.get_balance())
except Exception as e:
    print(e)

try:
    account1.deposit(3000)
    print("Name:", account1.get_account_holder(), "the current balance", account1.get_balance())
except Exception as e:
    print(str(e))
    print(account1.get_balance())

try:
    account1.withdraw(100)
    print("Name:", account1.get_account_holder(), "the current balance", account1.get_balance())
except Exception as e:
    print(e)