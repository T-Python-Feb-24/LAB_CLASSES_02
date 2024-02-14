from Bank import BankAccount

name = input("Enter your name: ")
print(f"Hello {name}, welcome to the bank!")
B1 = BankAccount(name,)

while True:
    print("-------------------------------")
    print("1. Check your Account Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")
    match choice:
        case "1":
            print("----------- Your Bank Account Info. ------------")
            print(f"Account Holder: {B1.get_account_holder()} \nInitial Balance: ${B1.get_balance()}\n")

        case "2":
            amount = int(input("Enter the amount of Depositing: "))
            print(f"After depositing, Account Holder: {B1.get_account_holder()}'s balance is: ${B1.deposit(amount)}\n")

        case "3":
            try:
                money = int(input("\nHow much would you like to withdraw? "))
                print(f"After withdrewing, Account Holder: {B1.get_account_holder()}'s balance is: ${B1.withdrew(money)}\n")
            except Exception as e:
                print(e)

        case "4":
            print("\nThank you for using our services!")
            break

        case _:
            print("\nInvalid Option. Please try again.")