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

# 2.1.2 Looping in GIS Models
import arcpy

try:
    arcpy.env.workspace = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson1"

    #list the feature classes in the Lesson 1 folder
    fcList = arcpy.ListFeatureClasses()

    #Loop through the list and copy the feature classes to the Lesson 2 PracticeData folder
    for featureclass in fcList:
        arcpy.CopyFeatures_management(featureclass, r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2\PracticeData\" + featureclass)

except:
    print "Script faled to complete"
    print arcpy.GetMessages(2)