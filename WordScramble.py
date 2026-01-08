import random

def wordScrambler():
    wordpool = ["Latitude", " arithmetic", " sophisticated", " pyscosis"]
    correctWord = ""
    randomSelect = random.randint(0,3)
    print(randomSelect)

    if randomSelect == 0:
        correctWord = wordpool[0]
    elif randomSelect == 1:
        correctWord = wordpool[1]
        
    elif randomSelect == 2:
        correctWord = wordpool[2]
        
    elif randomSelect == 3:
        correctWord = wordpool[3]
        

    convertedString = list(correctWord)
    random.shuffle(convertedString)
    scrambled = ''.join(convertedString)
    print(scrambled)
    userGuess = input("Please guess the correct word: ")
    while userGuess != correctWord:
        print("Incorrect password")
    attempts += 1
    print("number of attempts left:"  + str(attempts) +" / 3")
    if userGuess == correctWord:
        print("You Win!")
wordScrambler()