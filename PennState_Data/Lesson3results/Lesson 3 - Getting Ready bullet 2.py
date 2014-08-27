#Lesson 3 - Getting Ready bullet 2
# Try using an SQL expression with a search cursor to print the OBJECTIDs of all the park and rides in Chelan county (notice there is a County field that you could put in your SQL expression).

import arcpy
arcpy.env.workspace = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson3results\Lesson3PracticeExercises\Lesson3PracticeExerciseA\Washington.gdb"

#set variables
fc = "ParkAndRide"
tar_county = "King"
term_type ="Park & Ride"
field_county = "County"
field_type ="TYPE"
SQL = '"' + field_county + '" = ' + "'" + tar_county + "'" + " AND " + '"' + field_type + '" = ' + "'" + term_type + "'"
count = 0

#create search cursor
cursor = arcpy.SearchCursor(fc, SQL)
for row in cursor:
    print str(row.OBJECTID) + " " + str(row.County) + " " + str(row.TYPE)
    count += 1

print "There are " + str(count) + " " + str(term_type) + " in " + str(tar_county) + " county."

