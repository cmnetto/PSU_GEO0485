#Lesson 3 - Getting Ready bullet 3
#Use an update cursor to find the park and ride with OBJECTID 336. Assign it a ZIP code of 98512.


import arcpy

try:

    arcpy.env.workspace = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson3results\Lesson3PracticeExercises\Lesson3PracticeExerciseA\Washington.gdb"

    row, rows = None, None #this sets row and rows to something, if they are nothing yet.

    #set variables
    fc = "ParkAndRide"
    field = "Zipcode"
    oid = "OBJECTID"
    OID_number = "336" # this can be either in quotes or not. The SQL expresion needs to be a string, but do not make the final ouput in qoutes.
    zipCode = "98512"

    # To narrow down the rows to be edited...this can be used to look for just the effected rows.
    # be carefule with SQL statements .... had to cast
    # or change OID_number in the SQL exspression to str(OID_number) and remove all singlal quotes.
    # summary of change:   <SQL = '"' + oid + '" = ' + "'" + OID_number + "'"> was changed to <SQL = '"' + oid + '" = ' + str(OID_number)>
    SQL = '"' + oid + '" = ' + str(OID_number)
    #count = 0

    #create update cursor
    rows = arcpy.UpdateCursor(fc, SQL)
    row = rows.next()  #this is needed to start the cursor on the first row

    while row:
        row.setValue(field, zipCode) #change the field that needs to be updated
        rows.updateRow(row) #finialize edit
        row = rows.next()

    print "Success! - the field and value, " + field + " = " + zipCode + " In row " + oid + " = " + str(OID_number)

# When I wrote this, only God and I understood what I was doing
# Now, God only knows
except:
    arcpy.AddError("Could not complete process")
    print "Could not complete process"
    print arcpy.GetMessages()

# Even if the script fails, this will clean up the database or shapefile from
# anything that was created with this script.
finally:
    if row:
        del row
    if rows:
        del rows

