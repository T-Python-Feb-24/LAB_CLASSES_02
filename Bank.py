class BankAccount : 
    
    def __init__(self,account_holder,initial_balance=0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance
        
    
    def deposit(self,depositAmount):
        newBalance = self.initial_balance + depositAmount
        self.initial_balance = newBalance
        return newBalance
    
    def withdraw (self,widthrawAmount):
        newBalance =  self.initial_balance - widthrawAmount
        self.initial_balance = newBalance
        if widthrawAmount >self.initial_balance:
            raise Exception 
        return newBalance 
    
    def get_balance (self):
        return self.initial_balance 
    
    def get_account_holder(self):
        return self.account_holder
    
    


