#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     A Python script that reads the data from the spreadsheet and
# creates, from scratch, a polyline shapefile with n polylines, n being the
# number of rhinos in the spreadsheet. Each polyline should represent a rhino's
# track chronologically from the beginning of the spreadsheet to the end of the
# spreadsheet. Each polyline should also have a text attribute containing the
# rhino's name
#
# Author:      nettoc
# Created:     11/06/2014
# Copyright:   (c) BOEM Mapping and Automation Section nettoc 2014
# ArcGIS Version: 10.0
# Python Version: 2.6
#-------------------------------------------------------------------------------

import arcpy
arcpy.env.overwriteOutput = True

data = open(r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course" + \
"\PennState_Data\Lesson4results\Proj04_ParsingRhinoSightings\RhinoObservations.csv")
projFile = r"C:\Program Files (x86)\ArcGIS\Desktop10.0\Coordinate Systems\Projected Coordinate Systems" + \
"\World\WGS 1984 World Mercator.prj"
SR = arcpy.SpatialReference(projFile)

outpath = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course" + \
"\PennState_Data\Lesson4results\Proj04_ParsingRhinoSightings"
outname ="tracks.shp"

#create a blank polyline
arcpy.CreateFeatureclass_management(outpath, outname, "POLYLINE")
RTracks = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson4results\Proj04_ParsingRhinoSightings\tracks.shp"

# Create the "Name" field to hold each of the rhino's name
arcpy.AddField_management(RTracks, "Name", "TEXT")

# Read the first line and split out the header using ","
headerline = data.readline()
headerline = headerline.strip("\n")
valueList = headerline.split(",")

# Create an index for the headers, this assures that the data under eash named
# header will will be pulled even if the column is moved
observerIndex = valueList.index("Observer")
xIndex = valueList.index("X")
yIndex = valueList.index("Y")
RhinoIndex = valueList.index("Rhino")
NoteIndex = valueList.index("Comments")

# Create an empyt rhion dictionary
rhinoDict = {}
# Start the loop that will read each line after the header line
for line in data.readlines():
    line = line.strip("\n")
    sighting = line.split(",")

    # Create the variables fot the easch column
    RhinoName = sighting[RhinoIndex]
    xCoord = sighting[xIndex]
    yCoord = sighting[yIndex]
    comment = sighting[NoteIndex]
    # create the vertext from eash coord
    vertex = arcpy.Point(xCoord, yCoord)

    # Now the fun begins, as your looping through each line, your populating the
    # rhionDict, at first if the rhino's name is not in the dict add it with
    # an empty Array ie:  dict[name] = Array
    # I initially wanted to loop thourgh each name form a list, but found the "IF key NOT IN dictionary:" statement
    if RhinoName not in rhinoDict:
        rhinoDict[RhinoName] = arcpy.Array()

    # Add point object (vertex) to the array
    rhinoDict[RhinoName].add(vertex) # Use the dictionary object! THis is the same as saying Array.add(vertex), but your using the dict object
                                    # in other words rhinoDict[RhionName] = Array <Array is the item> so you get Array.add(vertex)
# Now insert the arrays from eash rhionDict key into the polyline
cursor = arcpy.InsertCursor(RTracks)
row = cursor.newRow()
for RhinoName in rhinoDict:
    row.shape = rhinoDict[RhinoName] # Use the dictionary object!
    row.Name = RhinoName
    cursor.insertRow(row)

del cursor
print "Complete! File location:  " + RTracks





