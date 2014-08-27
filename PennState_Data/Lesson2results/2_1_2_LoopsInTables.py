#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nettoc
#
# Created:     07/04/2014
# Copyright:   (c) nettoc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Loops in Tables
import arcpy
inTable = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2\CityBoundaries.shp"
inField = "NAME"

rows = arcpy.SearchCursor(inTable)

#This loop goes though each row in the table
#and gets a requested field value

for row in rows:
    correntCity = row.getValue(inField)
    print correntCity
