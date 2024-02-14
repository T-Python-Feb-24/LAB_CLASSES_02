class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
     self.account_holder=account_holder
     self.initial_balance=initial_balance

     def deposit(self,deposit_amount):
        INIBalance =self.initial_balance + deposit_amount
        self.initial_balance = INIBalance
        return INIBalance
     
     def withdraw(self,withdraw_amount):
        INIBalance =self.initial_balance -  withdraw_amount
        self.initial_balance = INIBalance
        if withdraw_amount > self.initial_balance:
           raise Exception
        return INIBalance
     
    def get_balance(self):
        return self.initial_balance
     
    def get_account_holder(self):
        return self.account_holder