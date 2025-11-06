# For Loops - A type of construct that runs code instructions
# a infinite amount of times over a group of data.

holloweenbag = ["Snickers", "KitKat", "Starburst", "Sour Patch Kids", "Candy Corn"]

count = len(holloweenbag)

print(count)

# i is a variable and is short for iterator
for i in holloweenbag:
    print(i)
    print(" I got this candy in my bag " + i)

# use a for loop to ask a user to type in 5 words and print each word out in
# the terminal. Once the user has finished typing 5 words,
# the for  loop should end.

for x in range(3):
    print("true or false: 3 is greater than 2")
    answer = input()
    if answer != True:
        print("great!")
        break
    else:
        print("wrong, try again")
        print("attempt" + str(x))
        print("true or false: 3 is greater than 2")
        answer = bool(input)

# Clarification: program should ask the user to type in 1 word. Then the program
# should print it out and ask the to type another word. Your program
# should do this 5 times.

for x in range(5):
    userword = input("Type in a word: ")
    print("You typed: " + userword) 