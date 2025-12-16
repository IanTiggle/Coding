def gpa_calculator():
    subject = input("Enter the subject area (): ")
    total_grade = 0
    weeks = 17

    for week in range(1, weeks + 1):
        while True:
            if subject.lower() in ["math", "science", "english"]:
                grade = float(input(f"Enter the grade for week {week}: "))
                if 0 <= grade <= 100:
                    total_grade += grade
                    break
                else:
                    print("Please enter a valid grade between 0 and 100.")
            else:
                print("Invalid input. Please enter a numerical grade.")

    average_grade = total_grade / weeks
    print(f"The average grade for {subject} over the semester is: {average_grade:.2f}")
    if average_grade >= 90:
        print("You got an A.")
    elif average_grade >= 80:
        print("You got a B.")
    elif average_grade >= 70:
        print("You got a C.")
    elif average_grade >= 60:
        print("You got a D.")
    else:
        print("You got an F.")
gpa_calculator()