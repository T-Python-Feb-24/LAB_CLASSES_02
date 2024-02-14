
class BankAccount:
    def __init__(self, account_holder:str, intial_balance:int = 0):
        self.__name = account_holder
        self.__balance = intial_balance
    
    def deposit(self, amount:int):
        self.__balance += amount
        return self.get_balance()

    def withdrew(self, amount:int):
        if self.__balance >= amount:
            self.__balance -= amount
            return self.get_balance()
        else:
            raise Exception(f"Insufficient funds. Your current balance: ${self.get_balance()}")

    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__name