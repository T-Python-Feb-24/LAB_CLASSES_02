class BankAccount:
    """
    This class represents a bank account with basic operations such as depositing, withdrawing, and checking the balance.
    """

    def __init__(self, account_holder_name: str, initial_balance: float = 0.0):
        """
        Initialize a new BankAccount instance with the given account holder name and initial balance.
        
        :param account_holder_name: The name of the account holder.
        :param initial_balance: The initial balance of the account. Default is 0.0.
        """
        self.__account_holder_name = account_holder_name  # The name of the account holder
        self.__blance = self.set_balance(
            initial_balance)  # The balance of the account

    def set_balance(self, balance: float):
        """
        Set the balance of the account.
        
        :param balance: The new balance of the account.
        :return: The new balance of the account.
        """
        if not isinstance(balance, (float, int)):  # Check if the balance is a float or an int
            raise ValueError("The balance must be a float")
        self.__blance = float(balance)  # Set the balance
        return float(balance)  # Return the balance

    def deposit(self, amount: float):
        """
        Deposit the given amount to the account.
        
        :param amount: The amount to deposit.
        :return: The new balance of the account.
        """
        self.__blance += amount  # Add the amount to the balance
        return self.__blance  # Return the new balance

    def withdraw(self, amount: float):
        """
        Withdraw the given amount from the account.
        
        :param amount: The amount to withdraw.
        :return: The new balance of the account.
        :raises ValueError: If the account does not have enough balance to cover the withdrawal.
        """
        if not self.__blance >= amount:  # Check if the balance is enough for the withdrawal
            raise ValueError("You can not withdraw more than what you have!!")
        else:
            self.__blance -= amount  # Subtract the amount from the balance
            return self.__blance  # Return the new balance

    def get_balance(self) -> float:
        """
        Get the current balance of the account.
        
        :return: The balance of the account.
        """
        return self.__blance  # Return the balance

    def get_account_holder(self) -> str:
        """
        Get the name of the account holder.
        
        :return: The name of the account holder.
        """
        return self.__account_holder_name  # Return the account holder name
