# 1 = rock, 2 = paper, 3 = scissors
import random
import os

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

def displayTrophy():
    print(" '._==_==_=_.'\n .-\:      /-.\n| (|:.     |) |\n '-|:.     |-'\n   \::.    /\n    '::. .'\n      ) (\n    _.' '._\n   `\"\"\"\"\"\"\"`")

def displaySadFace():
    print("     .-\"\"\"\"\"\"-.\n   .'          '.\n  /   O      O   \ \n :           `    :\n |                |\n :    .------.    :\n  \  '        '  /\n   '.          .'\n     '-......-'")

def displayDraw():
    print("________ __________    _____  __      __ \n\______ \\______   \  /  _  \/  \    /  \ \n |    |  \|       _/ /  /_\  \   \/\/   /\n |    `   \    |   \/    |    \        / \n/_______  /____|_  /\____|__  /\__/\  /  \n        \/       \/         \/      \/")

def instructions():
    print("You play against the computer. You can choose from three handsigns - Rock, Paper and Scissors")
    print("Rock beats scissors. Scissors beat paper. And paper beats rock.")
    print("When prompted, you have to enter 1 to choose rock, 2 to choose paper and 3 to choose scissors.")
    print("At the end if you have higher score than the computer you win.")

def startMsg():
    choice = int(input("Welcome to rock, paper scissors!\nEnter 1 to see instructions\nEnter 2 to continue:"))
    if(choice==1):
        instructions()  

def displayRock():
    print("    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)")

def displayPaper():
    print("    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)")

def displayScissors():
    print("    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)")
        
def playerChoose():
    choice = int(input("Choose your handsign:"))
    if(choice!=1 and choice!=2 and choice!=3):
        print("Invalid input.")
        playerChoose()
    else:
        if(choice==1):
            print("You chose rock!")
            displayRock()
        if(choice==2):
            print("You chose paper!")
            displayPaper()
        if(choice==3):
            print("You chose scissors!")
            displayScissors()
        return choice

def computerChoose(choice):
    if(choice==1):
        print("Computer chose rock.")
        displayRock()
    if(choice==2):
        print("Computer chose paper.")
        displayPaper()
    if(choice==3):
        print("Computer chose scissors.")
        displayScissors()

def WinCheck(pC, cC):   # pC = playerChoice , cC = computerChoice
    # 1 is PlayerWin, 2 is ComputerWin, 0 is Draw
    if(pC==1):
        if(cC==2):
            return 2
        elif(cC==3):
            return 1
        else:
            return 0

    if(pC==2):
        if(cC==1):
            return 1
        elif(cC==3):
            return 2
        else:
            return 0

    if(pC==3):
        if(cC==1):
            return 2
        elif(cC==2):
            return 1
        else:
            return 0

def scoreUpdate(roundWinner, playerScore, computerScore):
    if(roundWinner==1):
        playerScore+=1
    if(roundWinner==2):
        computerScore+=1
    return playerScore, computerScore
        
def endMsg(playerScore, computerScore):
    if(playerScore > computerScore):
        print("Congratulations! You win the game.")
        displayTrophy()
    elif(playerScore < computerScore):
        print("Sorry, you lost the game. Better luck next time.")
        displaySadFace()
    else:
        print("Draw game.")
        displayDraw()

def roundWinMsg(roundWinner):
    if(roundWinner==1):
        print("You win this round!")
    if(roundWinner==2):
        print("You lose this round.")
    if(roundWinner==0):
        print("Draw round")

def displayScore(playerScore, computerScore):
    print("Player: " + str(playerScore) + "\tComputer: " + str(computerScore) + "\n")

def chooseNumRounds():
    numRounds = int(input("Choose number of rounds (Cannot be more than 20):"))
    if(numRounds>20):
        print("Rounds cannot be more than 20. Choose again.")
        numRounds = chooseNumRounds()
    return numRounds
    
def gameloop():
    startMsg()
    choices = [1,2,3]
    playerScore = 0
    computerScore = 0
    numRounds = chooseNumRounds()
    for Round in range(numRounds):
        screen_clear()
        print("Round " + str(Round+1))
        print("Current Score")
        displayScore(playerScore, computerScore)
        print("Your turn.")
        playerChoice = playerChoose()
        computerChoice = random.choice(choices)
        computerChoose(computerChoice)
        roundWinner = WinCheck(playerChoice, computerChoice)
        roundWinMsg(roundWinner)
        playerScore, computerScore = scoreUpdate(roundWinner, playerScore, computerScore)
        input("Press enter key to continue...")
    screen_clear()
    print("Final Score")
    displayScore(playerScore, computerScore)
    endMsg(playerScore, computerScore)

choice = "y"
while(choice=="y" or choice=="Y"):
    screen_clear()
    gameloop()
    choice = str(input("Do you want to play again?(y/n):"))
    screen_clear()
    



        
