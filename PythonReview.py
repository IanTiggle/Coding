# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false.

def check_submission(class_work, homework):
    if class_work and homework:
        print("Both class work and homework have been submitted.")
    elif class_work:
        print("Only class work has been submitted.")
    elif homework:
        print("Only homework has been submitted.")
    else:
        print("Neither class work nor homework has been submitted.")
check_submission(True, False)

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    print(reversed_string)
print(reverse_string)

reverse_string("Hello, World!")

# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.

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