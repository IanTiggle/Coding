# Nested Conditions = Are if/ else blocks of code, that contain
# more if/ else blocks of code- conditions that have conditions

def coffeeshop():
    print("Welcome to the Coffee Shop. What would you like to order ?")
    print("1. hot drinks")
    print("2. cold drinks")
    print("3. snacks")
    print("4. hot food")
    select = int(input("What would you like to order? Please enter a number: "))
    if select == "1":
        print("You have selected hot drinks. What type of hot drink would you like?")
        print("1. Coffee")
        print("2. Tea")
        print("3. Hot Chocolate")
        drink = int(input("select a drink: "))
        if drink == "1":
            print("would you like a S, M, L, XL?")
        if drink == "2":
            print("which flavor would you like?")
            print("1. peach")
            print("2. green")
            print("3. earl grey")
            
        


def atm():
    balance = 5000
    pin = 1234
    print("Welcome to the ATM machine. Please type in your pin.")
    userPin = int(input())
    if userPin == pin:
        print("what would you like to do?")
        print("1. withdraw")
        print("2. deposit")
        print("3. check balance")
        select = int(input("select an option: "))
        if select == 1:
            print("how much would you like to withdraw?")
            amount = int(input())
            newBalance = balance - amount
            print("you are taking out : " + str(amount))
            print("your new balance is : " + str(newBalance))
            if amount > balance:
                print("Overdraft! You do not have enough money in your account.")
        if select == 2:
            print("how much would you like to deposit?")
            amount = int(input())
            newBalance = balance + amount
            print("you are depositing : " + str(amount))
            print("your new balance is : " + str(newBalance))
        if select == 3:
            print("your balance is : " + str(balance))
        else:
            print("invalid option, please try again.")
        
               
                
    else:
        print("the pin you have entered is incorrect, please try again.")
        atm()

atm()
