#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
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

#create a blank polyline
outpath = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course" + \
"\PennState_Data\Lesson4results\Proj04_ParsingRhinoSightings"
outname ="tracks.shp"
##RTracks = arcpy.CreateFeatureclass_management(outpath, outname, "POLYLINE")
RTracks = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course" + \
"\PennState_Data\Lesson4results\Proj04_ParsingRhinoSightings\PolyLine4.shp"

# Loop and delete any existing features in the shapefile this is only used while trouble shooting
rows = arcpy.UpdateCursor(RTracks)

for row in rows:
    rows.deleteRow(row)
del rows
print "Prepairing shape file..."
#-------------


#-------------------------
# This function checks to see if a name is in the rhinoList, if not it add it.
def RhioNameListMaker(name, List):
    if name in List:
        pass
    else:
        List.append(name)
#-------------------------
# This function will add each create a new polyline and create the track of each rhion
##def addPolyline(cursor, array, spaRef):
##    feature = cursor.newRow()
##    polyline = arcpy.Polyline(array, spaRef)
##    feature.SHAPE = polyline
##    cursor.insertRow(feature)
##    array.removeAll()

#-------------------------
def addArrayToDict(key, array, dictionary):
    if key in dictionary:
        pass
    else:
        dictionary[key] = array
#-------------------------

headerline = data.readline()
headerline = headerline.strip("\n")
valueList = headerline.split(",")

observerIndex = valueList.index("Observer")
xIndex = valueList.index("X")
yIndex = valueList.index("Y")
RhinoIndex = valueList.index("Rhino")
NoteIndex = valueList.index("Comments")


rhinoList = []
rhinoDict = {}

# Call funstion to create a list of the rhino names
cursor = arcpy.InsertCursor(RTracks)
coordArray = arcpy.Array()

for line in data.readlines():
    line = line.strip("\n")
    sighting = line.split(",")

    # Create an empty Array for the vertecies

    RhinoName = sighting[RhinoIndex]
    xCoord = sighting[xIndex]
    yCoord = sighting[yIndex]
    comment = sighting[NoteIndex]

    RhioNameListMaker(RhinoName, rhinoList)

    for name in rhinoList:


        if name == RhinoName:
            print "MATCH" + name + ", " + RhinoName
            vertex = arcpy.Point(xCoord, yCoord)
            coordArray.add(vertex)
        elif name != RhinoName:
            print "NO match " + name + ", " + RhinoName

        else:
            pass
        addArrayToDict(name, coordArray, rhinoDict)


##        print name, RhinoName, xCoord, yCoord, coordArray

for name in rhinoList:
    feature = cursor.newRow()
    array = rhinoDict[name]
    feature.SHAPE = array
    feature.Name = name
    cursor.insertRow(feature)



##for name in rhinoList:
##    addPolyline(cursor, rhinoDict[name], SR)
del cursor




print rhinoDict
##print valueList
##print rhinoList



