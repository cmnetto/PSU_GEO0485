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

import arcpy

inputfc = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson1\Nebraska.shp"

desc = arcpy.Describe(inputfc)
typefc = desc.shapeType

print "This shapeile is a " + typefc + "."