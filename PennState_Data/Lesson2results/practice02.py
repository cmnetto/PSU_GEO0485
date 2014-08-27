#Lesson 2 Practice Exercise 02
#Convert the names to a "Last, First" format-
#Build on Exercise 1 by printing each name in the list in the following format:
#Last, First

beatles = ["John Lennon", "Paul McCartney", "Ringo Star", "George Harrison"]

for name in beatles:
    space = name.index(" ")
    last = name[space:]   # the solution used this 'last = member[space+1:]', the author's solution eliminates the a space in at the begining of the last name.
    first = name[:space]
    print last + ", " + first

