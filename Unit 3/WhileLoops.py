# While Loop definition - a while loop is a type of construct
# where code instructions will keep on running so
# long as a condition is TRUE (boolean)

# NOTE - In order to stop a loop (or any program) from running
# in your terminal, click ctrl + c at the same time.

# While Loop Syntax

ageVerification = 17
purchaser = int(input("Enter your age: "))

while purchaser <= ageVerification: #17 >= 15 = TRUE: 17 is larger than 15
    print("Sorry, you're not old enough")
else:
    print(" Enjoy your collecters edition of GTA VI")

savepassword = "123abc"
userpassword = input("Enter your password: ")
attempts = 0
profilemenu = ["Photos, Videos, Friends"]

while userpassword != savepassword: 
    print("Incorrect password")
    attempts += 1
    print("number of attempts left:"  + str(attempts) +" / 3")
    userpassword = input("Enter your password: ")
    if attempts == 3:
        print("Too many attempts, account locked for 5 minutes")
        break


else:
    print("Welcome to your account!")
    

number = 0
while number <= 10:
    print(number)
    number += 1
else:
    print("Done counting")

# Create a countdown timer using a while.
# your timer should start at 30 and count down to 0 by 1.

timer = 30
while timer >= 0:
    print(timer)
    timer -= 1
else:
    print("Time's up")