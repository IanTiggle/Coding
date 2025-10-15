#Question 1

def canVote(age):

    if age >= 18:
        print("you can get vote in the upcoming election.")
    else: 
        print("you cannot vote in the upcoming, you are not old enough.")

canVote(17)

#Question 2

def LargestNum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the largest number.")
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is the largest number.")
    else:
        print(f"{num3} is the largest number.")

LargestNum(30, 22, 67)

#Question 3

def TicketPrice(age):
    if age <= 13:
        print("Your ticket price is $10.00.")
    elif age >= 14:
        print("Your ticket price is $15.00.")
    elif age >=25:
        print("Your ticket price is $20.00.")
    elif age >= 55:
        print("Your ticket price is $10.00.")
    else:
        print("Your ticket price is $13.00.")

TicketPrice(14)