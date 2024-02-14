# LAB_CLASSES_02


# Create a Python class called `BankAccount` that simulates a simple bank account. 
# The class should have the following functionalities:
class BankAccount:

# 1. It should have a constructor that accepts the `account_holder` name and 
# initial balance (`initial_balance`), setting the balance to zero if the initial 
# balance is not provided.
    def __init__(self , account_holder: str , initial_balance : float = 0) :
        self.account_holder = account_holder
        self.initial_balance = initial_balance

# 2. A method called `deposit` that accepts an amount and adds it to 
# the account balance, and then returns the updated balance.
    def deposit(self, amount) : 
       self.initial_balance += amount
       return self.initial_balance
       
    def withdraw(self, amount):
        if self.initial_balance >=amount:
            self.initial_balance -= amount 
            return self.initial_balance
        else:
            raise Exception ("Insufficient funds")
        
# 4. A method called `get_balance` that returns the current account balance.
    def get_balance(self):
       return self.initial_balance


# 5. A method called `get_account_holder` that returns the name 
# # of the account holder.
    def get_account_holder(self):
        return f"I am {self.account_holder} the account holder"
