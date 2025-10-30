def numberLoop():
    numbers = []
    userNumber = (input("Enter a Number: "))
    while userNumber != "quit":
        transformNumber = int(userNumber)
        numbers.append(transformNumber)
        print(numbers)
        userNumber = (input("Enter a Number: ")) 
    else:
        print("the loop has stopped")

#numberLoop()

def numberaddition():
    total = 0
    userNumber = (input("Enter a Number: "))
    while userNumber != "quit":
        transformNumber = int(userNumber)
        total += transformNumber
        print("The total is: " + str(total))
        userNumber = (input("Enter a Number: ")) 
    else:
        print("the loop has stopped")
#numberaddition()


def numberguesser():
    secretnumber = 7
    userguess = int(input("Guess the secret number between 1 and 10: "))
    while userguess != secretnumber:
        if userguess < secretnumber:
            print("Too low! Try again.")
        elif userguess > secretnumber:
            print("Too high! Try again.")
        userguess = int(input("Guess the secret number between 1 and 10: "))
    else:
        print("Congratulations! You guessed the secret number.")

numberguesser()