def Fooditems():
    Fooditems = ["Pizza", "Burger", "Pasta", "Salad"]
    print(Fooditems [0])
    print(Fooditems [3])
    Fooditems.remove("Burger")
    Fooditems.insert(1, "Sushi")
    Fooditems.remove("Pizza")
    Fooditems.remove("Salad")
    print(Fooditems)
#Fooditems()


def restaurantmenu():
    print("Welcome to the restaurant. Enter what time of day it is.:")
    time = input("1. breakfast, 2. lunch, 3. dinner: ")
    if time == "Morning":
        print("Here is our breakfast options")
        print(["pancakes", "waffles", "omelette"])
    elif time == "Afternoon":
        print("Here is our lunch options")
        print(["BLT", "Chicken Sandwich", "Caesar Salad"])
    elif time == "Night":
        print("Here is our dinner options")
        print(["Spaghetti", "Alfredo", "Chicken Parmesan"])
    else:
        print("Invalid option, please try again.")
restaurantmenu()
