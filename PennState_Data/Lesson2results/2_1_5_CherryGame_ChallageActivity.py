#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      nettoc
#
# Created:     07/04/2014
# Copyright:   (c) nettoc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# 2.1.5 Putting it all togehter

# Simulates one game of Hi Ho! Cherry-O

import random, time

start_time = time.time()

spinnerChoices = [-1, -2, -3, -4, 2, 2, 10]
turns = 0
cherriesOnTree = 10
outLoop = 1
averageList = []
games = 10

#because this games will based on an indexed number we need to add one in order for the
#numbers reflect the correct unmber of games in the print statements.
numOfGames = games + 1

#creatioutloopxted loop to figure the average number of spins it takes to win

while outLoop < numOfGames:
        print "--------Get Ready, Starting Game " + str(outLoop)
        # Take a turn as long as you have more than 0 cherries
        while cherriesOnTree > 0:
            # Spin the spinner
            spinIndex = random.randrange(0, 7)
            spinResult = spinnerChoices[spinIndex]


            # Print the spin result
            print "You spun " + str(spinResult) + "."

            # Add or remove cherries based on the result
            cherriesOnTree += spinResult

            # Make sure the number of cherries is between 0 and 10
            if cherriesOnTree > 10:
                cherriesOnTree = 10
            elif cherriesOnTree < 0:
                cherriesOnTree = 0

            # Print the number of cherries on the tree
            print "You have " + str(cherriesOnTree) + " cherries on your tree."

            turns += 1

        #add the number of turns to a list, which will be used to calculate the average later
        averageList += [turns]

        # Print the number of turns it took to win the game
        print "It took you " + str(turns) + " turns to win the game."

        #reset all the numbers in the game
        cherriesOnTree = 10
        turns = 0
        ##lastline = raw_input("Enter your name")
        ##print "Congradulations " + lastline + " you are a WINNER!!"
        #this is needed to keep the loop of games moving forward
        outLoop +=1

averageOfTurnsII = sum(averageList)/games
averageOfTurns = sum(averageList)/len(averageList)
runTime = time.time() - start_time
print "----THANK YOU FOR PLAYING CHERRYTREE----"
print "   __.--~~.,-.__"
print "   `~-._.-(`-.__`-."
print "           \    `~~`"
print "      .--./ |"
print "     /#   \  \.--."
print "     \    |  /#   |"
print "      '--'   \    /"
print "              '--'"
#print "Over" + str(numOfGames) + " games, it took you and avage of " +  + " to win."
print "Out of " + str(games) + " games, it took you an average of " + str(averageOfTurns) + " turns to win each game"
print "It took this computer " + str(runTime) + " seconds to run this script"
