# Condtional Statements - code instructions that
# have different outcomes based on the imputted data.
# input --> condition --> output

# Conditional Statment Syntax
# if keyword - Controls the condition we want to satisfy

# else keyword - Our default outcome. The thing that 
# happens when our condition is NOT satisfied.

weather = input("What is the weather like today? ")
if weather == "sunny":
    print(" It is beautiful outside. Bring sunglasses.")
else:
    print("I can't tell you the weather, but have a good day.")
if weather == "rainy":
    print("Remeber to bring an umbrella.")
elif weather == "snowy":
    print("Wear warm clothes.")
elif weather == "cloudy":
    print("It might be a bit gloomy today.")
elif weather == "windy":
    print("Hold onto your hat!")
elif weather == "chilly":
    print("Wear a jacket.")

password = input("Please enter your password: ")
if password == "abc123":
    print("Welcome! You are now logged in.")
else: 
    print("Access denied, Try Again.")

vanilla = 0
chocolate = 10
strawberry = 10

def iceCreamShop(flavor):
    if vanilla > 1:
        print("We have that in stock.")
    elif chocolate > 1:
        print("We have that in stock.")
    elif strawberry > 1:
        print("We have that in stock.")
    else:
        print("we don't have that ice cream.")

#iceCreamShop("vanilla")

down = input("What down is it? ")
yards = int(input("How many yards to go? "))

if down == 1 and yards <= 5:
    print("Run the ball.")
elif down == 2 and yards <= 5:
    print("Run the ball.")
elif down == 3 and yards <= 5:
    print("play action.")
else:
    print("punt")

def permit(age):

    if age >= 16:
        print("you can get a permit.")
    else: 
        print("you cannot get a permit, you are not old enough.")

#permit(17)

def numbercheck(number):
    if number > 0:
        print("This is a positive number.")
    elif number < 0:
        print("This is a negative number.")
    else:
        print("Zero")

numbercheck(80)

def Gradecalc(grade):
    if grade >= 90:
        print("You got an A.")
    elif grade >= 80:
        print("You got a B.")
    elif grade >= 70:
        print("You got a C.")
    else:
        print("You got an F.")

Gradecalc(69)