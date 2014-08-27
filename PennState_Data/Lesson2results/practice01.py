#Lesson 2 Practice Exercise 01
#Find the spaces in a list of names-
#Then write code that will loop through all the items in the list, printing a message like the following:
#"There is a space in ________'s name at character ____."

beatles = ["John Lennon", "Paul McCartney", "Ringo Star", "George Harrison"]

for name in beatles:
    space = name.index(" ")
    print "There is a space in " + str(name) + "'s name at character " + str(space)
