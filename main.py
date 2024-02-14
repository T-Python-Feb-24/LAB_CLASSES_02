from bank import BankAccount

account1= BankAccount("Lama",5000)

print(account1.get_account_holder())
print(account1.get_balance())
print(account1.deposit(400))
 
try:
  print(account1.withdraw(6000)) 
except Exception as e:
  print(e)

