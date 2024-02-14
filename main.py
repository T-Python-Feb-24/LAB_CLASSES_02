# Importing the BankAccount class from the bank_account module
from bank_account import BankAccount

# Defining the account holder's name and initial balance
account_holder_name: str = "wissam"
balance: float = float(100)

# try block
try:
    # Creating an instance of the BankAccount class with the account holder's name
    account1: BankAccount = BankAccount(account_holder_name)

    # Printing the account holder's name
    print(f"The name of the account holder is {account1.get_account_holder()}")

    # Printing the initial balance
    print(f"The amount balance {account1.get_balance()}")

    # Defining the amount to be withdrawn
    withdrow_amount: float = float(150)

    # Attempting to withdraw the specified amount
    print(account1.withdraw(withdrow_amount))

    # The following block of code will handle any exceptions that occur during execution
except Exception as e:
    # Printing the exception message
    print(e)
