class BankAccount:
    def __init__(self, account_holder:str,initial_balance:int =0 ):
        self.set_account_holder(account_holder)
        self.set_balance(initial_balance)

    def deposit(self, deposit_amount):
        self.__initial_balance += deposit_amount
        return self.__initial_balance
        

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__initial_balance:
            raise Exception(f"Your balance is ({self.get_balance()}) insufficient to complete the withdrawal process.")
        self.__initial_balance -= withdraw_amount
        return self.__initial_balance
        
    def get_balance(self):
        return self.__initial_balance
    
    def set_balance(self, initial_balance:int):
        if not isinstance(initial_balance, int):
            raise Exception("The balance amount must be intger number only.")
        self.__initial_balance = initial_balance

    def get_account_holder(self):
        return self.__account_holder
    
    def set_account_holder(self, account_holder:str):
        if not isinstance(account_holder, str):
            raise Exception("The account holder must be sting only.")
        self.__account_holder = account_holder


    

    

