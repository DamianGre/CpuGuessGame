import random

again = True
print("It's a number guessing game. User will pick random number from range 0-100 and Cpu need to pick this number. \nIf You want to end game during game enter 'quit' instead of number")
while again:
    print("New Game has started")
    triesCounter=1
    userNumber = "a"
    cpuNumber = ""
    while userNumber != cpuNumber:
        userAnswer =""
        userNumber = input("Enter number:  ")
        while userNumber.isdigit() == False:
            if userNumber.lower() == "quit":
                again = False
                print("End of the game.")
                break
            print("You have entered wrong data, insert digits")
            userNumber = input("Enter number: ")

        if userNumber.lower() == "quit":
            break
        if userNumber.lower() != "quit":
            userNumber = int(userNumber)
            if userNumber < 0:
                print("User number is lower then 0. User can set number just from range 0-100. Change range")
                continue
            if userNumber > 100:
                print("User number is higer then 100. User can set number just from range 0-100. Change range")
                continue
            cpuNumber = random.randint(1, 100)
            cpuUpperBorder = 100
            cpuLowerBorder = 1

            while userAnswer.lower() != "right":
                if cpuNumber == userNumber:
                    print("Cpu number is", cpuNumber, "and Your number is", userNumber)
                    print("WIN! Cpu number and Your number is same! CONGRATULATIONS")
                    print("Number of tries counter = " + str(triesCounter))
                    break
                print("Cpu number is", cpuNumber, "\nEnter lower(if Cpu number is lower then Your number),\n"
                                                 "Enter higher(if Cpu number is higher then Your number),\n"
                                                 "Enter right(if number same as Your number)\n")
                userAnswer = input()
                if userAnswer.lower() == "lower":
                    cpuUpperBorder = cpuNumber-1
                    cpuNumber = random.randint(cpuLowerBorder, cpuUpperBorder)
                    triesCounter += 1
                elif userAnswer.lower() == "higher":
                    cpuLowerBorder = cpuNumber+1
                    cpuNumber = random.randint(cpuLowerBorder, cpuUpperBorder)
                    triesCounter += 1
                elif userAnswer.lower() == "right":
                    print("WINNER! Your number is same as cpu number! CONGRATULATIONS")
                    print("Number of tries counter = " + str(triesCounter))
        if str(cpuNumber).lower() != "quit":
            playAgain = ""
            while playAgain != "no" and playAgain != "yes":
                playAgain = input("Do You want to play again? yes/no")
                if playAgain.lower() == "no":
                    again = False
                    print("End of the game.")
                elif playAgain.lower() == "yes":
                    break
                else:
                    print("wrong input")
