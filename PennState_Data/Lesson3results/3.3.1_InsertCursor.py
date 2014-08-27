#3.3.2 Inserting new records

import arcpy

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

rows = arcpy.UpdateCursor(incidentsFC)

for row in rows:
    rows.deleteRow(row)
    print "rows deleted"

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