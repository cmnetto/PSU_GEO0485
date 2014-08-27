#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nettoc
#
# Created:     07/04/2014
# Copyright:   (c) nettoc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# Nested Loops
suits = ['Spades', 'Clubs', 'diamonds', 'Hearts']
values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
for suit in suits:
    for val in values:
        print str(val) + " of " + str(suit)


