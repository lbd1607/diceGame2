#Laura Davis
#21 March 2016
#CGP145 Ch06 Lab-3 The Dice Game
#This program is a two player game that will assign a random number
#to each player, compare the values, and declare a winner or a tie.
#add libraries needed
import random 
#This is the main function
def main():
    print
    #Intitialize variables
    endProgram = "no"
    #Call to inputNames
    playerOne, playerTwo = inputNames()
    #While loop to run program again
    while endProgram == "no":
        #Call to roll dice
        winnerName, p1number, p2number = rollDice(playerOne, playerTwo)
        #Call to displayInfo
        displayInfo(winnerName, p1number, p2number, playerOne, playerTwo)
        endProgram = raw_input("Do you want to end the program? (Enter yes or no): ")
		
#This function gets the players' names
def inputNames():
    playerOne = raw_input("Player One Enter your name: ")
    playerTwo = raw_input("Player Two Enter your name: ")
    return playerOne, playerTwo
	
#This function will get the random values
def rollDice(playerOne, playerTwo):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6) 
    if p1number == p2number:
        winnerName = "TIE"
    elif p1number > p2number:
        winnerName = playerOne
    else:
        winnerName = playerTwo
    return winnerName
    return p1number
    return p2number
		
#This function displays the winner
def displayInfo(winnerName, p1number, p2number, playerOne, playerTwo):
    print "The winner is ", winnerName
    print playerOne,"'s roll is ", p1number
    print playerTwo,"'s roll is ", p2number
#Calls main
main()
