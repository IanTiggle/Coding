#How to create a function that passes data

# Step 1. create a function definition
def bnbRefund(username, refundAmount):
    print("sorry "+ username + ", for your cancellation")
    print("We will refund $" + str(refundAmount) + " amount to your bank.")


# Step 2. Call the function/ insrtructions
bnbRefund(" Jacob" , 3000)


def birthday(name, date):
    print("My name is" + name + date )

birthday(" Ian", " My birthday is February 27th")

def dollartopenny(dollars):
    pennies = dollars * 100
    print("My " + str(dollars) + " dollar(s) is equal to " + str (pennies) + " pennies.")
dollartopenny(300)


def triangleArea(width, length):
    area = length * width * 0.5
    print("The area of a triangle with the width of " + str(width) + " and length of " + str(length) + " is equal to " + str(area))
triangleArea(15, 20)

def triangleArea2(length, width, height):
    area = length * width * height
    print("The area of a triangle with the width of " + str(width) + " and length of " + str(length) + " and height of " + str(height) + " is equal to " + str(area))
triangleArea2(20, 30 , 60)

def temperatureconvter(farenheit):
    celsius = (farenheit * 5/9) -32
    print("The temperature of " + str(celsius) + " degrees celsius is equal to " + str(farenheit) + " degrees farenheit.")
temperatureconvter(100)



def multiplication(num1):
    product = num1 * 10
    input("Enter a number: ")
    print(str(num1) + "* " +  " = " + str(product))
multiplication(10)