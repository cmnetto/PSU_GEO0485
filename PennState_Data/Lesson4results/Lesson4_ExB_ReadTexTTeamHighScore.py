# Lesson 4 Practice Exercise B
# Write a script that reads a text file and List the team names, followed by the
# maxium number of goals scored in a game.

scoresText = open(r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson4results\Lesson4PracticeExerciseB\Scores.txt")
TeamScores = {}  #create an empty dictionary {TeamName:goals}
winner = 0
winnerGoals = 0
loser = 0
loserGoals = 0

# ------------------------------------------
# Check the number os goals scored and if its higher, add it to the dictionary
def goalchecker(team, goals, dictionary):
    #Check if the team has a key in the dictionary
    if team in dictionary:
        #if a key (team name) was found, check goals against team's current max in the dictionary
        if goals > dictionary[team]:
            dictionary[team] = goals
        else:
            pass
    # if no key found, add one with the current number of goals
    else:
        dictionary[team] = goals
# ------------------------------------------

# Read the headers and seperate into a list
headerLine = scoresText.readline()
# remove the the \n from the last line in the test file.
headerLine = headerLine.rstrip("\n")
valueList = headerLine.split(" ")

# Create an index for all the values, this will make easier to break out all the
#   scores later
WinnerNameIndex = valueList.index("Winner")
WinnerGoalsIndex = valueList.index("WG")
LoserNameIndex = valueList.index("Loser")
LoserGoalsIndex = valueList.index("LG")

# Read easch line and break out each game
for line in scoresText.readlines():
    line = line.rstrip("\n") # **need to remove this AGAIN, since its reading each line. this is the "new line" charater put in by Notepad
    game = line.split(" ")

    Winner = game[WinnerNameIndex]
    winnerGoals = game[WinnerGoalsIndex]
    Loser = game[LoserNameIndex]
    loserGoals = game[LoserGoalsIndex]

    # Using the function above check the winners and losers scores for the max value within this loop
    goalchecker(Winner, winnerGoals, TeamScores)

    goalchecker(Loser, loserGoals, TeamScores)

for key in TeamScores:
    print key + ":" + TeamScores[key]






