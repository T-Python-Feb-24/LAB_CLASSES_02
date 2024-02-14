from bank import BankAccount

account = BankAccount("Rahaf",100)
print("Balance Before deposit:",account.get_balance())

print(account.get_balance())

try:
    account.withdraw(400)
except Exception as e :
    print(e)


print("Balance After Withdraw:",account.get_balance())
print(f"Account Holder: {account.get_account_holder()}, INIBalance: {account.get_balance()}")