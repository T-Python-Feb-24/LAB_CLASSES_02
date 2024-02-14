
class BancAccount ():
    def __init__(self , first_name:str ,last_name:str,balance:float =0.00 ) -> None:
        self.first_name=first_name
        self.balance=balance
        self.last_name=last_name
        

    def deposit (self , amount):
        self.amount=amount
        udeposit_balance= self.amount + self.balance
        return udeposit_balance
        
    def get_balance (self):
        return f"Current account balance is : {self.balance}"

    def get_account_holder (self):
        return f"Name of account holder is : {self.first_name} {self.last_name}"
    
    
    def withdraw (self , amount):
        self.amount=amount

        if self.balance == 0:
            raise Exception("The balance is not allowed , less than the required limit")
        else:
            withdraw_balance= self.balance - amount
            return withdraw_balance

    

