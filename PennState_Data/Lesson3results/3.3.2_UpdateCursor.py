# 3.3.1 Updating existing records

#simple search and replace script
import arcpy

# Retrieve input parameters: the feature class, the field affected by
#  the search and replace, the search term, and the replace term.

fc = arcpy.GetParameterAsText(0)
affectedField = arcpy.GetParameterAsText(1)
oldValue = arcpy.GetParameterAsText(2)
newValue = arcpy.GetParameterAsText(3)

# Create the SQL expression for the update cursor. Here this is
#  done on a separate line for readability.

# "affectedField" = 'oldValue'
queryString = '"' + affectedField + '" = ' + "'" + oldValue + "'"

# Create the update cursor and advance the cursor to the first row
rows = arcpy.UpdateCursor(fc, queryString)
row = rows.next()

# Perform the update and move to the next row as long as there are
#  rows left

While row:
    row.SetValue(affectedField, newValue)
    rows.updateRow(row)
    row = rows.next()

# Delete the cursors to remove any data locks
del row, rows
