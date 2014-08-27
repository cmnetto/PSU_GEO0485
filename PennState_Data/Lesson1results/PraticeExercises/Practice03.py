#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nettoc
#
# Created:     01/04/2014
# Copyright:   (c) nettoc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

try:
    name = raw_input("Enter Yo Name")
    hi = "hello"
    #s = hi + " " + name

except:
    arcpy.AddError("Sorry this didnt run correctly")

print(hi + " " + name)