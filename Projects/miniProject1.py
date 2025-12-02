# Build a Python program that presents users with 5 multiple-choice questions.
# For each question, the user should be able to input their selection from a list of options.
# The program should keep track of their answers. 
# Once the user answers all questions , display the user's score by showing them
# the number of answers they got correct out of 5.
# The questions should be about python programming language.
def quiz():
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["1. .pyth", "2. .pt", "3. .py", "4. .pyt"],
            "answer": 3
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["1. func", "2. def", "3. function", "4. define"],
            "answer": 2
        },
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": ["1. // This is a comment", "2. /* This is a comment */", "3. # This is a comment", "4. <!-- This is a comment -->"],
            "answer": 3
        },
        {
            "question": "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
            "options": ["1. ptrim()", "2. strip()", "3. len()", "4. trim()"],
            "answer": 2
        },
        {
            "question": "Which operator is used to multiply numbers in Python?",
            "options": ["1. x", "2. *", "3. %", "4. #"],
            "answer": 2
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = int(input("Please enter the number of your answer: "))
        if user_answer == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print("Wrong! The correct answer was option number {}\n".format(q["answer"]))

    print("You got {} out of {} correct.".format(score, len(questions)))
quiz()