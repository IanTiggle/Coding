# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

# 1. Name and describe three (3) built-in functions in python. 
# Please write your responses in complete sentences.
"One built-in function in python is the print() function. This function is used to output text or other data types to the console or terminal." 
"Another built-in function is the input() function, which allows the program to take user input from the terminal as a string." 
"A third built-in function is the len() function, which returns the length of a string, list, or other iterable data types."
# 2. What data type will the following snippet of code output?
print(30/ 232)
"The data type will be a float because it becomes a decimal number."
# 3.  Identify and name the operator family each of the following
# symbols belongs to.

# and 
"The 'and' operator belongs to the logical operator family."
# ==
"The '==' operator belongs to the comparison operator family."
# >
"The '>' operator belongs to the comparison operator family."
# 4. Explain the difference between the = operator and the == operator.
# Please write your response in complete sentences.
"The '=' operator is used for assignment, meaning it assigns a value to a variable."
"The '==' operator is used for comparison, meaning it checks if two values are equal."
# 5. Write code that takes a user’s input (as a string), 
# casts it to a float, and prints the result multiplied by 2.
print(float(input("Enter a number: ")) * 2)

# 6. What is the difference between a parameter and an argument?
# Please write your response in complete sentences.
"A parameter is a variable that is defined in the function definition and acts as a placeholder for the value that will be passed to the function when it is called."
" An argument, on the other hand, is the actual value that is passed to the function when it is invoked."
" In other words, parameters are used in the function definition, while arguments are used in the function call."
# 7. What is the difference between a function definition 
# and a function invocation? # Please write your response in 
# complete sentences.
"A function definition is the process of creating a function by specifying its name, parameters, and the block of code that will be executed when the function is called. It essentially defines what the function does."
"A function invocation, also known as a function call, is the process of executing a function that"
# 8. Why are functions useful in programming? Provide at least two reasons 
# and write your reasons in in complete sentences.
"Functions are useful in programming because they allow for code reusability."
"Once a function is defined, it can be called multiple times throughout the program without having to rewrite the same code, which saves time and reduces redundancy."
# 9. Write a code block that uses the appropriate operator for each scenario
x = 15
y = 20.
# x is greater than y
# x and 15 are both the same
# x and y are not the same`
x>y
x==15
x!=y
# 10. Create a function that will take in two values. Your function should
# take in 1 value as a parameter, and the other value should be passed in by the
# user through the terminal. Your function should compare if the number passed in by
# the user is greater than the number passed in via the parameter and should print out
# the appropriat response of true or false.

def comparison(parameter):
    uservalue = float(input("Enter a number: "))
    print(uservalue > parameter)

comparison(10)