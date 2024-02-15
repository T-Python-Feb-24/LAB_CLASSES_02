class BankAccount:
    def __init__(self, name: str, account_holder: str, initial_balance: float = 0) -> None:
        self.name = name
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float):
        self.balance += amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

    def withdraw(self, amount: float):
        if self.balance < amount:
            raise Exception("Insufficient funds")
        self.balance -= amount
        return self.balance