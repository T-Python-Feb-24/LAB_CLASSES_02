class bank_account:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount
        return self.get_balance()

    def withdraw(self, withdrawn_amount):
        self.withdrawn_amount = withdrawn_amount
        if self.balance >= withdrawn_amount:
            self.balance -= withdrawn_amount
            return self.get_balance()
        else:
            raise Exception("Insufficient funds to withdraw this amount.")

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder
    
    def account_display(self):
        return f"Account holder: {self.account_holder} account balance: {self.balance}"
    
    def deposit_display(self):
        return f"Deposited amount: {self.deposit_amount}"
    
    def withrdaw_display(self):
        return f"Withdrawn amount: {self.withdrawn_amount}"