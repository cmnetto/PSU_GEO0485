#3.2.4 Retrieving Records using a spatial query

#Selects all the states whose boundaries touch a user suppplied state

import arcpy

#Get the US States layer, state and state name field
usalayer = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2results\Lesson2PracticeExercise\Lesson2PracticeExercise\USA.gdb\State_boundaries"
state = "Wyoming"
nameField = "NAME"

try:
    #Make a feature layer with all the US States
    arcpy.MakeFeatureLayer_management(usalayer, "AllStatesLayer")

    #Make a feateur layer containging only the state of interest using a SQL expression
    arcpy.MakeFeatureLayer_management(usalayer, "SelectionStateLayer", '"' + str(nameField) + '" =' + "'" + str(state) + "'")

    #Apply a selection to the US States Layer
    arcpy.SelectLayerByLocation_management("AllStatesLayer", "BOUNDARY_TOUCHES", "SelectionStateLayer")

    #Open a search cursor on the US States Layer
    rows = arcpy.SearchCursor("AllStatesLayer")
    row = rows.next()

    #Print the name of all the staets in the selection
    while row:
        print row.getValue(nameField)
        row = rows.next()

    #Clean house
    del row
    del rows

except:
    print arcpy.GetMessages()

# Clean up feature layers
arcpy.Delete_management("AllStatesLayer")
arcpy.Delete_management("SelectionStateLayer")