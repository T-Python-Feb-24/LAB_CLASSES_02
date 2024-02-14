class BankAccount:
    def __init__(self,account_holder:str,initial_balance:float=0):
        self.account_holder=account_holder
        self.initial_balance=initial_balance

    def deposit(self,amount):
        '''
        to add money
        '''
        if isinstance(amount,float):
            self.initial_balance+=amount
          
        elif isinstance(amount,int):
            self.initial_balance+=amount
            
        else:
            raise Exception("Make sure you entered a number")
        
    def withdraw(self,amount):
        '''
        to withdraw money
        '''
        if self.initial_balance<amount:
            raise Exception("There is not enough money and the current balance:")
        else:
            self.initial_balance-=amount
            
    def get_balance(self):
        return self.initial_balance
    def get_account_holder(self):
        return self.account_holder
        


        