#Lesson 3 - Getting Ready bullet 1
# Try to loop through the CityBoundaries and print the name of each city.

import arcpy
arcpy.env.workspace = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson3results\Lesson3PracticeExercises\Lesson3PracticeExerciseA\Washington.gdb"

#set variables
fc = "CityBoundaries"

#create search cursor
cursor = arcpy.SearchCursor(fc)
for row in cursor:
    print row.Name

print "complete"

