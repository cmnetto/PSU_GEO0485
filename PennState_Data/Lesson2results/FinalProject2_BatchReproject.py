# Lesson 2 Project
# Project 2: Batch reprojection tool for vector datasets
# Requirements:
# -Must re-project shapefile vector datasets in the folder to match the target dataset's projection.
# -Must append "_projected" to the end of each projected dataset name. For example: CityBoundaries_projected.shp.
# -Must skip projecting any datasets that are already in the target projection.
#   Must report a geoprocessing message telling which datasets were projected.
#   In this message, the dataset names can be separated by spaces. In the
#   message, do not include datasets that were skipped because they were already
#   in the target projection. Notice an example of this type of custom message
#   below in the line "Projected . . . :"
# -Must not contain any hard-coded values such as dataset names, path names, or
#   projection names.
# -ust be made available as a script tool that can be easily run from ArcToolbox
#   by someone with no knowledge of scripting.

import arcpy
from arcpy import env

try:
    tar_dir = arcpy.GetParameterAsText(0)
    tar_src = arcpy.GetParameterAsText(1)
    #tar_dir = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2"
    #tar_src = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2\CityBoundaries.shp"
    env.workspace = tar_dir
    sr_target = arcpy.Describe(tar_src).spatialReference
    arcpy.env.overwriteOutput = True
    proj_list = []

    fclist = arcpy.ListFeatureClasses()
    for fc in fclist:
        sr = arcpy.Describe(fc).spatialReference
        if sr.name == sr_target.name:
            #print fc + " has the same spatial reference as " + sr_target.name
            print arcpy.AddMessage(fc + " spatial reference matched and does not need a reprojection")
        else:
            #print fc + " NEEDS to be changed"
            arcpy.CreateFolder_management(tar_dir, "projected")
            rootname = ""
            if fc.endswith(".shp"):
                rootname = fc[:-4]
            out_dataset = "/projected/" + rootname + "_projected.shp"
            arcpy.Project_management(fc, out_dataset, sr_target)
            #print fc + " HAS been projected"
            print arcpy.AddMessage(fc + " HAS been projected")
            #proj_list += [fc]
    #print arcpy.AddMessage("The following were reprojected" + proj_list)

except:
    arcpy.AddError("Could not complete process")
    print "Could not complete process"
    print arcpy.GetMessages()
