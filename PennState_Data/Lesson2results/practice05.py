# Lesson 2 Practice Exercise 05
# Find the spaces in a list of names-
# Your task is to write a script that programmatically clips all the feature
# classes in the USA geodatabase to the Iowa state boundary. The clipped feature
# classes should be written to the Iowa geodatabase. Append "Iowa" to the
# beginning of all the clipped feature class names.

# Your script should be flexible enough that it could handle any number of
# feature classes in the USA geodatabase. For example, if there were 15 feature
# classes in the USA geodatabase instead of three, your final code should not\
# need to change in any way.



import arcpy


from arcpy import env
env.workspace = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2\Lesson2PracticeExercise\Lesson2PracticeExercise\USA.gdb"
arcpy.env.overwriteOutput = True

try:
    #list all the fc in the USA gdb
    fcList = arcpy.ListFeatureClasses()
    #get the number of itesm and print them for the user (this only to give the user visual que)
    numItems = len(fcList)
    print "There are " + str(numItems) + " items to be clipped"

    #fc used to clip to
    clipfc = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2\Lesson2PracticeExercise\Lesson2PracticeExercise\Iowa.gdb\Iowa"
    #Loop through the fc's and print status for the user
    for fc in fcList:
        outfc = clipfc + "_" + fc
        arcpy.Clip_analysis(fc, clipfc, outfc)
        print"completed clipping " +  fc
    print "PROCESS COMPLETE!"

except:
    print "Script failed to complete"
    print arcpy.GetMessages() #this message comes from the ESRI GP tools
    arcpy.AddError("Could not clip feature classes")#if you were running this as a tool on ArcGIS, this would display in the ArcGIS dialog

#When you make a script tool, take out the print statements and add the arcpy.AddMessage and arcpy.AddError functions, so that your messages will appear in the ArcGIS tool results window.


##Answer from Book - https://www.e-education.psu.edu/geog485/L02_Prac5.html
###This script clips all feature classes in a file geodatabase
##
##import arcpy
##
### Create path variables
##sourceWorkspace = "C:\\Data\\Lesson2PracticeExercise\\USA.gdb"
##targetWorkspace = "C:\\Data\\Lesson2PracticeExercise\\Iowa.gdb"
##clipFeature = "C:\\Data\\Lesson2PracticeExercise\\Iowa.gdb\\Iowa"
##
### Get a list of all feature classes in the USA folder
##arcpy.env.workspace = sourceWorkspace
##featureClassList = arcpy.ListFeatureClasses()
##
##try:
##
##    # Loop through all USA feature classes
##    for featureClass in featureClassList:
##
##        # Construct the output path
##        outClipFeatureClass = targetWorkspace + "\\Iowa" + featureClass
##
##        # Perform the clip and report what happened
##        arcpy.Clip_analysis(featureClass, clipFeature, outClipFeatureClass)
##        arcpy.AddMessage("Wrote clipped file " + outClipFeatureClass + ". ")
##        print "Wrote clipped file " + outClipFeatureClass + ". "
##
##except:
##
##    # Report if there was an error
##    arcpy.AddError("Could not clip feature classes")
##    print "Could not clip feature classes"
##    print arcpy.GetMessages()