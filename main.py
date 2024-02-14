from bank_class import BankAccount

user_list = [
    {'Hammam': 500.00},
    {'Razan': 0.00},
    {'Khaled': 100.00},
    {'Mohamed':2500},
    {'Rahmah':27.99},
    {'Abdullah':88.77}
]

def operation(username, user_list, user_instances) -> BankAccount:
    for user_instance in user_instances:
        if user_instance.get_account_holder() == username:
            return user_instance
    
    for user in user_list:
         if username in user:
            user_ = BankAccount(username, user[username])
            return user_
    else:
        user_balance = float(input("You don't have an account. Enter your balance: "))
        user_ = BankAccount(username, user_balance)
        user_instances.append(user_)
        return user_

user_instances = []
username = input('Enter Your Name here: ')
while True:
    try:
        print('-----Welcome To Our Bank-----')
        print('select 1- To deposit \n2- To withdraw \n3- to get the account balance \n4- to exit')
        user_choice:int = int(input('Please enter your choice here: '))
        if user_choice == 1:
            user_ = operation(username, user_list, user_instances)
            print(f'The user {user_.get_account_holder()} has an account balance: ${user_.get_balance()}')
            amount:float = float(input('Please Enter the amount you want to deposit: '))
            user_.deposit(amount)
            print(f'Now in the account of user: {user_.get_account_holder()} the balance is ${user_.get_balance()}')
        elif user_choice == 2:
            user_ = operation(username, user_list, user_instances)
            print(f'The user {user_.get_account_holder()} has an account balance: ${user_.get_balance()}')
            amount:float = float(input('Please Enter the amount you want to withdraw: '))
            user_.withdraw(amount)
            print(f'Now in the account of user: {user_.get_account_holder()} the balance is ${user_.get_balance()}')
        elif user_choice == 3:
            user_ = operation(username, user_list, user_instances)
            print(f'The account balance is: ${user_.get_balance()}')
        elif user_choice == 4:
            print('Thanks For Using Our Bank. See You Again!')
            break
        else:
            print('You entered a wrong data. Please try again..')
    except Exception as e:
        print(e)
