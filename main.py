from BankAccount import BankAccount
account1=BankAccount("rayan")
print("name:",account1.get_account_holder(),"and the current balance:",account1.get_balance())

try:
    update_balance=account1.deposit(990)
    print("name:",account1.get_account_holder(),"and the current balance:",account1.get_balance())
except Exception as e:
    print(str(e))

update_balance=account1.withdraw(500)
print("name:",account1.get_account_holder(),"and the current balance:",account1.get_balance())

try:
    update_balance=account1.withdraw(1000)
    print("name:",account1.get_account_holder(),"and the current balance:",account1.get_balance())

except Exception as e:
    print(str(e))
    print(account1.get_balance())
update_balance=account1.withdraw(100)
print("name:",account1.get_account_holder(),"and the current balance:",account1.get_balance())








