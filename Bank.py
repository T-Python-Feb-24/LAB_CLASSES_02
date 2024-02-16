class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

account = BankAccount("John Doe", 1000)
print(account.get_balance()) 

account.deposit(500)
print(account.get_balance())  

account.withdraw(200)
print(account.get_balance())  

account.withdraw(1500)  
print(account.get_balance())  