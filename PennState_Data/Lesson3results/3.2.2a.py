# Finds the average population in a counties dataset

import arcpy

#featureClass =

# Finds the average population in a counties dataset

# use raw_input if not using ArcGIS, use GetPara....if using ArcGIS
#featureClass =  raw_input("inter the feature classe path")
arcpy.GetParameterAsText(0)
#populationField = raw_input("enter the population field")
arcpy.GetParameterAsText(1)

rows = arcpy.SearchCursor(featureClass)
row = rows.next()

average = 0
totalPopulation = 0
recordsCounted = 0

# Loop through each row and keep running total of population
#  and records counted.

while row:
    totalPopulation += row.getValue(populationField)
    recordsCounted += 1
    row = rows.next()

average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)
