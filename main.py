from BankAccount import BankAccount
import sys

account_holder = None

while True:
    print("-" * 40)
    print("1- Check your Account")
    print("2- Deposit")
    print("3- Withdraw")
    print("4- Exit")
    print("-" * 40)

    choice = input("Choose an option: ")

    if choice == "1":
        if account_holder is None:
            name = input("Enter your name: ")
            account_holder = BankAccount(name, "Account Holder")  # Provide the necessary arguments
        print("-" * 40)
        print(f"Account Holder: {account_holder.get_account_holder()}\nInitial Balance: {account_holder.get_balance()}\n")
        print("-" * 40)

    elif choice == "2":
        if account_holder is None:
            print("Please check your account balance.")
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            new_balance = account_holder.deposit(amount)
            print("-" * 40)
            print(f"After depositing, {account_holder.get_account_holder()} balance is: {new_balance}\n")
            print("-" * 40)

    elif choice == "3":
        if account_holder is None:
            print("Please check your account balance.")
        else:
            try:
                amount = int(input("Enter the amount you want to withdraw: "))
                new_balance = account_holder.withdraw(amount)
                print("-" * 40)
                print(f"After withdrawal, {account_holder.get_account_holder()} balance is: {new_balance}\n")
                print("-" * 40)
            except Exception as e:
                print(e)
                print("-" * 40)

    elif choice == "4":
        print("\nWe appreciate you utilizing our services!")
        print("-" * 40)
        sys.exit()  # Exit the program

    else:
        print("\nError. Please try again.")
        print("-" * 40)