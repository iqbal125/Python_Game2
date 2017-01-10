#Create You own quiz

print "Hello and welcome to the python quiz. All questions will be fill in the blank."
user_input = input("Please select difficulty of quiz, easy | medium | hard: ")

while True:
    if user_input == "easy":
        UseEasyGame();
        break
    elif user_input == "medium":
        UseMediumGame();
        break
    elif user_input == "hard":
        UseHardGame();
        break
    else:
        print ("I don't understand, Please select difficulty")




#Easy Game Counter
EasyGameCount = 0

#Easy Game function
def UseEasyGame():
    #To Loop Through the questions
    while EasyGameCount < 4:
        easy1q = input("To print the number 7 you will type print(__)")
        #To Loop through 1 question
        while True:
            if easy1q == easy1a:
                print (easy1a + " is Correct!")
                EasyGameCount = EasyGameCount + 1
                break
            else:
                print ("Sorry, try again")
        easy2q = input("To print the word hello you will type __(hello), enter as string")
        while True:
            if easy2q == easy2a:
                print (easy2a + " is Correct!")
                EasyGameCount = EasyGameCount + 1
                break
            else:
                print ("Sorry, try again")
        easy3q = input("Control flow uses an __ statement")
        while True:
            if easy3q == easy3a:
                print (easy3a + " is Correct!")
                EasyGameCount = EasyGameCount + 1
                break
            else:
                print ("Sorry, try again")
        easy4q = input("A collection of elements is a __")
        while True:
            if easy4q == easy4a:
                print (easy4a + " is Correct!")
                EasyGameCount = EasyGameCount + 1
                break
            else:
                print ("Sorry, try again")

#Medium Game Counter
MediumGameCount = 0

#Medium Game Funtion
def UseMediumGame():
    #To Loop Through the questions
    while MediumGameCount < 4:
        med1q = input("A true or false statement will print __")
        #To Loop Through 1 question
        while True:
            if med1q == med1a:
                print (med1a + " is Correct!")
                MediumGameCount = MediumGameCount + 1
                break
            else:
                print ("Sorry, try again")
        med2q = input("A true and False statement will print __")
        while True:
            if med2q == med2a:
                print (med2a + " is Correct!")
                MediumGameCount = MediumGameCount + 1
                break
            else:
                print ("Sorry, try again")
        med3q = input("to print the length of a list you use the __ function")
        while True:
            if med3q == med3a:
                print (med3a + " is Correct!")
                MediumGameCount = MediumGameCount + 1
                break
            else:
                print ("Sorry, try again")
        med4q = input("A function starts with the word __")
        while True:
            if med4q == med4a:
                print (med4a + " is Correct!")
                MediumGameCount = MediumGameCount + 1
                break
            else:
                print ("Sorry, try again")

#Hard Game Counter
HardGameCount = 0

#Hard Game Function
def UseHardGame():
    #To Loop through the questions
    while HardGameCount < 4:
        hard1q = input("To iterate over a list you use a __ loop")
        if hard1q == hard1a:
            print (hard1a + " is Correct!")
            HardGameCount = HardGameCount + 1
            break
        else:
            print ("Sorry, try again")
        hard2q = input("True and false statements are known as __")
        if hard2q == hard2a:
            print (hard2a + " is Correct!")
            HardGameCount = HardGameCount + 1
            break
        else:
            print ("Sorry, try again")
        hard3q = input("The dominant paradigm programmers use is __ oriented programming")
        if hard3q == hard3a:
            print (hard3a + " is Correct!")
            HardGameCount = HardGameCount + 1
            break
        else:
            print ("Sorry, try again")
        hard4q = input("The __ statement executes a code as long as a certain condition is true")
        if hard4q == hard4a:
            print (hard4a + " is Correct!")
            HardGameCount = HardGameCount + 1
            break
        else:
            print ("Sorry, try again")
























#Questions and Answers

#Easy Game Questions
#easy1q = input("To print the number 7 you will type print(__)")
#easy2q = input("To print the word hello you will type __(hello), enter as string")
#easy3q = input("Control flow uses an __ statement")
#easy4q = input("A collection of elements is a __")

#Easy Game Answers
easy1a = 7
easy2a = "print"
easy3a = "if"
easy4a = "list"


#Medium Game Questions
#med1q = input("A true or false statement will print __")
#med2q = input("A true and False statement will print __")
#med3q = input("to print the length of a list you use the __ function")
#med4q = input("A function starts with the word __")

#Medium Game Answers
med1a = "true"
med2a = "false"
med3a = "len"
med4a = "def"


#Hard Game Questions
#hard1q = input("To iterate over a list you use a __ loop")
#hard2q = input("True and false statements are known as __")
#hard3q = input("The dominant paradigm programmers use is __ oriented programming")
#hard4q = input("The __ statement executes a code as long as a certain condition is true")

#Hard Game Answers
hard1a = "for"
hard2a = "booleans"
hard3a = "object"
hard4a = "while"
