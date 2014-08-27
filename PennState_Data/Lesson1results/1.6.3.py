# this script was created for lesson 1.6.3
import arcpy
from arcpy.sa import *

inRaster = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson1\foxlake"
cutoffElev = 3500

arcpy.CheckOutExtension("Spatial")

outRaster = Raster(inRaster) > cutoffElev
outRaster.save(r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson1\foxlakeNET")

arcpy.CheckInExtension("Spatial")
