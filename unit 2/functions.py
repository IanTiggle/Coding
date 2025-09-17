# Function: is a set of code instructions labeled under a custom name
# that the computer will run

#Function Syntax (rules of how its written)
# functions have 2 phases: function definition and function call

#phase 1: fuction definition
# we are describing the instructions for our custom code
# we are adding logic to the computers vocabulary
# this code will not run- it only give the computer the meaning
# not the action 

def example():
    print("good morning.") # 1 instruction: print good morning

    #phase 2: function call
    # once we have the definition, we can now run the instructions
    # by writing the funtion name.

    example() 
# we indent to inform the computer that we are about to write
# code instructions. if we don't, we will get an error
    def example2():
        print("good afternoon.")
        a=input(" enter a number")
        print(a)

    example2()

    def math():
        a = input("enter a number")
        b = 30
        print("Here is your answer!")
        print(int(a) + b)   
#math()



#create a function that will calculate 2 numbers
#with different arithmetic operators

def calculate():
    Numx = input("enter a number : ")
    Numy = input("enter another number : ")
    print(Numx, Numy)
        
calculate()
    