from Bank import BankAccount

accountOne = BankAccount("SHEKHA",5000)
print("Balance Before deposit:",accountOne.get_balance())

accountOne.deposit(4000)
print("Balance After Deposit:",accountOne.get_balance())

try:
    accountOne.withdraw(10000)
except Exception as e :
    print(e)


print("Balance After Withdraw:",accountOne.get_balance())
print(f"Account Holder: {accountOne.get_account_holder()}, Balance: {accountOne.get_balance()}")



