# 4.3 Writing geometries
# The following is the example used in the course, but converted from 10.1 to 10.0.
# from the section "Creating a polyline from a GPS track"
# https://www.e-education.psu.edu/geog485/node/142

import arcpy
arcpy.overwriteoutput = True


out_path = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson4results\4_3"
polylineFC = "PolylineFromArray.shp"
geoType = "POLYLINE"
SR = r"C:\Program Files (x86)\ArcGIS\Desktop10.0\Coordinate Systems\Projected Coordinate Systems\World\WGS 1984 World Mercator.prj"
gpsTrack = open(r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson4results\gps_track.txt", "r")
count = 0
#Create a shapefile
arcpy.CreateFeatureclass_management(out_path, polylineFC, geoType, "", "", "", SR)

# Figure out position of lat and long in the header
headerLine = gpsTrack.readline()
valueList = headerLine.split(",")

latValueIndex = valueList.index("lat")
longValueIndex = valueList.index("long")

# Create the Array to store the point for the polyline
vertexArray = arcpy.Array()

# Read each line in the file
for line in gpsTrack.readlines():
    segmentedLine = line.split(",")

    # Get the lat/long values of the current GPS reading
    latValue = segmentedLine[latValueIndex]
    longValue = segmentedLine[longValueIndex]

    # Create a point and add it to the array
    vertex = arcpy.Point(longValue, latValue)
    vertexArray.add(vertex)

    # keep count of the points beging added
    count += 1

# Create the insert cursor
rowInserter = arcpy.InsertCursor(polylineFC)
newIncident = rowInserter.newRow()

# Use the newly created Array to populate the SHAPE field
newIncident.SHAPE = vertexArray

# Insert the new row into th shapefile
rowInserter.insertRow(newIncident)

# Clean up anything that can cause a lock on the shapefile
del rowInserter

print count



