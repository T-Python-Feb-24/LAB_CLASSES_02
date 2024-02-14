class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.00) -> None:
        self.account_holder = account_holder
        self.account_balance = initial_balance

    def deposit(self, amount: float) -> float:
        self.account_balance += amount

    def withdraw(self, amount: float) -> float:
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Sorry it seems like there -> Insufficient funds.")
    
    def get_balance(self):
        return self.account_balance

    def get_account_holder(self):
        return self.account_holder
