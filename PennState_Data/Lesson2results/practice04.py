# Lesson 2 Practice Exercise 04
# Create copies of a template shapefile-


#set up script
import arcpy
from arcpy import env
arcpy.overwriteoutput = True
out_path = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2results"
out_name = "PrecipReadings"
template = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson1\Precip2008Readings.shp"
env.workspace = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2results"
out_name_year = 2009

try:
    while out_name_year < 2013:
        name = out_name + str(out_name_year)
        arcpy.CreateFeatureclass_management (out_path, name, "", template,)
        print str(out_name) + str(out_name_year) + " copied and creaeted"
        out_name_year += 1
except:
    print arcpy.GetMessages()

#The books solution
#import arcpy
#
#try:
#    arcpy.env.workspace =  "C:\\Data\\"
#
#    template = "Precip2008Readings.shp"
#
#    for year in range(2009,2013):
#        newfile = "Precip" + str(year) + "Readings.shp"
#        arcpy.CreateFeatureclass_management(arcpy.env.workspace, newfile, "POINT", template)
#
#except:
#    print arcpy.GetMessages()