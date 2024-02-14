from bank_account import BancAccount

try:
   person1=BancAccount("Ahmad" , "Alabady",00.00)
   person2=BancAccount("Hala" , "Alfayz",18000.00)
   person3=BancAccount("Ahlam" , "Fahad",9000.00)
   person4=BancAccount("Khalid" , "Almansorry",25000.00)
   person5=BancAccount("Waad" , "Alanzi")


   print(person5.get_balance())
   print(person2.get_balance())
   print(person3.get_account_holder())
   print(person4.get_account_holder())
   print(person2.deposit(500))
   print(person4.deposit(1200))
   print(person3.deposit(1000))
   print(person5.deposit(5000))
   print(person2.withdraw(200))
   print(person4.withdraw(700))
   print(person1.withdraw(300))


except Exception as e:
    print(e)