# Lists - A system for collecting and organizing multiple pieces of data.

# List syntax (How it is written)
# When we want to create a list, we first create a variable name
# and assign it to the square brackets [].
# we then put the data we want to collect inside of the square brackets.

shopingCart = ["water", "ice", "cereal", "apples"]

# Accessing items in a list-
# When we want to access an item in a list we write the variable name
# and then use the square brackets and pass in the item postion in the brackets.

# python is a zero-based index language, meaning when counting items,
# zero is treated as an actual numbers and is counted.

print(shopingCart[3])

def addItemtoCart():
    bestBuyCart = ["8k monitor", "graphics card", "speakers", "pro controller"]

    item = input("Please add new item): ")

    print(bestBuyCart)
def removeItemfromCart():
    bestBuyCart = ["8k monitor", "graphics card", "speakers", "pro controller"]

    item = input("Please remove item): ")
    bestBuyCart.remove(item)
    print(bestBuyCart)
def numberList(number):
    numbersList = [100, 23, 450, 63, 1, 6, 19, 1000]
    numbersList.append(number)
    numbersList.sort()
    print(numbersList)

numberList(60)
