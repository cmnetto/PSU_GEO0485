# Lesson 4 Practice Exercise A
# Write a script that reads a text file and creates a state bounary polygon out the
# coordinates supplied in the text file.

# 1. Open text file
# 2. Read the lines and split them by x and y
# 3. then split each x and y and group them.
# 4.



import arcpy
arcpy.env.overwriteOutput = True

boundaryTxt = open(r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson4results\Lesson4PracticeExerciseA\MysteryStatePoints.txt")
StateFC = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson4results\Lesson4PracticeExerciseA\MysteryState.shp"
count = 0
print"loaded variables"
# Split out the data in the text file into seperate x and y using the delimiter "|"
AllLines = boundaryTxt.readline()
valueList = AllLines.split("|")
print valueList
try:
    # Create an ESRI array
    vertexArray = arcpy.Array()

    # Read each line in the file, then
    for line in valueList:
        segmentedLine = line.split(",")

        # Create a point and add it to an array
        vertex = arcpy.Point(segmentedLine[0], segmentedLine[1])
        vertexArray.add(vertex)
       # Keep count of the points added
        count +=1
    # Open the insert cursor
    cursor = arcpy.InsertCursor(StateFC)
    # create a new row in this cursor
    row = cursor.newRow()

    # Use the newly created Array to propulate the SHAPE feild
    row.SHAPE = vertexArray

    # Insert the new row into the shapefile
    cursor.insertRow(row)

    print "Complete. Added " + str(count) + " vertices"

except:
    arcpy.AddError("Could not complete process")
    print "Could not complete process"
    print arcpy.GetMessages()

# Even if the script fails, this will clean up the database or shapefile from anything that was created with this script.
finally:
    if row:
        del row
    if cursor:
        del cursor
