from bank_Account import BankAccount




holder1 = BankAccount("Mohammed" , 100.000)
holder2 = BankAccount("Abdullah" , 50.000)

print(holder1.account_holder , holder1.initial_balance )
print(holder2.account_holder , holder2.initial_balance )


print(holder1.deposit(10.000))
print(holder1.withdraw(20.000))
print(holder1.get_account_holder())
print(holder1.get_balance())

print(holder2.deposit(300.000))
print(holder2.withdraw(95.000))
print(holder2.get_account_holder())
print(holder2.get_balance())