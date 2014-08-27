# Lesson 4 Practice Exercise C
#  Your task is to print the average length of the name of each animal type

# function to load dictionarydef BuildDictionary():
def BuildDictionary():
   #create lists
   dogList = ["Dalmatian", "German Shepherd"]
   catList = ["American Shorthair"]
   birdList = ["Robin", "Canary","Bluebird" ]

   #use dict() constructor to create dictionary and add keys and values
   return dict([('dogs', dogList), ('cats', catList), ('birds', birdList)])

# Call the function and assign the result to the variable 'animals'.
animalsDict = BuildDictionary()
# New code to print the average length of the animal names for each animal type
# (dogs, cats, and birds) should be inserted after this line.


print "The following looks at a dictionary and calclates the average number of letters in \
each of the dictionary's items. (Animal type = key, Breed = items)"
animalList = animalsDict.keys() # Put the dict keys into a list
print animalsDict

# This first loop will loop throught each key
for types in animalsDict: # Loop through the keys ("types")
    breedLetterCount = 0.0 #define a floating point number, so we dont have to use "float()" later on
    breedcount = 0.0

    # This nested loop will loop through each item, within the keys and count the number of letters
    for breed in animalsDict[types]: # loop through each key, which is defined by "types" variable for this iteration of the first loop
        currentcount = len(breed) # keep count of the letters in the current interation of the 2nd loop
        breedLetterCount += currentcount # add the current count of letters to a running toral of all the letters in the items from the interation of the 1st loop
        breedcount += 1 # keep track of the number of items in each key
        average = breedLetterCount/breedcount # get the average

    print "Total Letters in the " + str(types) + " type: " + str(breedLetterCount)
    print "Number of breeds in " + str(types) + " (items): " + str(breedcount)
    print "Average number of letters of all the breeds in the " + types + " group: " + str(average)

