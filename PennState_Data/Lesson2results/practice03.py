# Lesson 2 Practice Exercise 03
# Convert scores to letter grades
# Write a script that accepts a score from 1-100 as an input parameter,
# then reports the letter grade for that score

input = raw_input("Enter a score between 0 and 100")
#The values coming are str so you have to turn them into int
score = int(input)

if score > 89:
    print "Grad A - Super Star"
elif score > 79:
    print "B"
elif score > 69:
    print "C"
elif score > 59:
    print "D"
else:
    print "Failed - Better Luck Next Time"
