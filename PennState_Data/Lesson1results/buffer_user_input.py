#1.6.4 and 1.7.1

import arcpy
arcpy.env.overwriteOutput = True

try:
    #Get all the input values
    inPath = arcpy.GetParameterAsText(0)
    outPath = arcpy.GetParameterAsText(1)
    bufferDistance = arcpy.GetParameterAsText(2)

    #Run the buffer tool
    arcpy.Buffer_analysis(inPath, outPath, bufferDistance)

    #Success Message
    arcpy.AddMessage("The buffer is complete!")

except:
    arcpy.AddError("Could not complete the buffer")

    arcpy.AddMessagee(arcpy.GetMessage())



