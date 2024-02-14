class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)):
            self.initial_balance += amount
        else:
            raise Exception("Make sure you enter a number")

    def withdraw(self, amount):
        if self.initial_balance < amount:
            raise Exception(f"There is not enough money. The current balance is: {self.initial_balance}")
        else:
            self.initial_balance -= amount

    def get_balance(self):
        return self.initial_balance

    def get_account_holder(self):
        return self.account_holder