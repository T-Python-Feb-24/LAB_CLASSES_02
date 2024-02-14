from bank_account import bank_account

account1 = bank_account("Salem", 1000)
account1.deposit(500)
account1.withdraw(200)

account2 = bank_account("ali", 10000)
account2.deposit(1000)
account2.withdraw(5000)

print(account1.account_display())
print(account1.deposit_display())
print(account1.withrdaw_display())

print(account2.account_display())
print(account2.deposit_display())
print(account2.withrdaw_display())