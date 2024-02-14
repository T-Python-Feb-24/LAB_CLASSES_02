
#Create a Python class called `BankAccount`
class BankAccount:
  

  def __init__(self,account_holder,initial_balance=0) -> None:
    self.account_holder= account_holder
    self.initial_balance= initial_balance


  def deposit(self,account_balance):
        self.initial_balance  += account_balance
        return self.initial_balance

  def withdraw(self,account_balance): # try .. Exception استخدمت في ملف المين
      if account_balance > self.initial_balance:
          raise Exception("there are insufficient funds")
      self.initial_balance  -= account_balance
      return self.initial_balance  
      
     

  def get_balance(self):
     return self.initial_balance
  

  def get_account_holder(self):
      return self.account_holder
  
  