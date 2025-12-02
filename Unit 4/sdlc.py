keywords = ["nfl", "nba", "anime", "games" ]
instagram = []

for post in instagram:
    

    
    searchbar = input("What are you looking for today? ")
"nfl hoodies"
for word in keywords:
    results = word
    print("we found this content for you: " + str(results))



"My calculator should be able to subtract multiple numbers and give me the total."
"My calculator should be able to divide multipe numbers and transform them into floats."
"My calculator should be able to multiply multiple numbers and give me the total."

def calculator():
    operation = input("What would youj like to do? (add, subtract, multiply, divide) ")
    if operation == "add":
        numbers = input("Enter numbers to add, separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        total = sum(num_list)
        print("The total is: " + str(total))
    elif operation == "subtract":
        numbers = input("Enter numbers to subtract, separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        total = num_list[0]
        for num in num_list[1:]:
            total -= num
        print("The total is: " + str(total))
    elif operation == "multiply":
        numbers = input("Enter numbers to multiply, separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        total = 1
        for num in num_list:
            total *= num
        print("The total is: " + str(total))
    elif operation == "divide":
        numbers = input("Enter numbers to divide, separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        total = num_list[0]
        for num in num_list[1:]:
            total /= num
        print("The total is: " + str(total))
    else:
        print("Invalid operation.")
calculator()