import random
"My game should be able to play rock, paper, scissors"
"My game should evaluate the winner based on the inputs"
"My game should be abble to play against the computer"
"My game should keep going until the user stops it"

def rps():

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        if user_choice == 'quit':
            print("You have quit rps.")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
rps()



def rpsGame():

    choices = ["rock", "paper", "scissors"]
    print("Welcome to RPS : the Game!")
    print("***************************")
    print("Please select from the following options: ")
    print("1. Start Game")
    print("2. Game Rules")
    print("3. Quit")
    selection = int(input)
    if int(selection) == 1: 
        print("Starting Game...")
        print("Please select a game mode: ")
        print("1. vs. human")
        print("2. vs. cpu")
        gameMode = int(input)
        if int(gameMode) == 1:
            print("Coming soon. sorry : / )")
        else: 
            print("Game is starting....")
            print("************************")
            print("Please make a selection: ")
            print("1. rock")
            print("2. paper")
            print("3. scissors")
            userSelection = int(input)
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

    elif int(selection) == 2:
        print("Game Rules....")
    elif int(selection) == 3:
        print("Goodbye!")
    else:
        print("ERROR, Invalid selection, please a listed option from the menu.")
