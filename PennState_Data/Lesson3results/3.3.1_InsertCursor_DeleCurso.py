#3.3.2 Inserting new records
# This script will open a point file, delete any current points in it, then insert the point specifed by the user.
import arcpy
arcpy.overwriteoutput = True

# Retrieve input parameters
##inX = arcpy.GetParameterAsText(0)
##inY = arcpy.GetParameterAsText(1)
##inDescription = arcpy.GetParameterAsText(2)

inX = raw_input("enter X")
inY = raw_input("enter Y")
inDescription = raw_input("enter description")



# These parameters are hard-coded. User can't change them.
incidentsFC = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2results\Lesson2PracticeExercise\Lesson2PracticeExercise\USA.gdb\Lesson3_Point"
descriptionField = "DESCR"

#Open the Update Cursor (Delete)
rows = arcpy.UpdateCursor(incidentsFC)

#Start a loop to print the Description field to be deleted and delete the row
for row in rows:
    name = row.DESCR
    print name
    rows.deleteRow(row)
    print "The row with description " + name + " has been deleted"

#Clean up the variables
del row, rows

# Create point
inPoint = arcpy.Point(inX, inY)

# Create the insert cursor and a new empty row
rowInserter = arcpy.InsertCursor(incidentsFC)
newIncident = rowInserter.newRow()

# Populate attributes of new row
newIncident.SHAPE = inPoint
newIncident.setValue(descriptionField, inDescription)

# Insert the new row into the shapefile
rowInserter.insertRow(newIncident)

#Clean UP
del rowInserter