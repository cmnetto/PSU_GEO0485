# 4.1 Functions and modules
# Creating a Mudule

# This module is save as practiceModule1.py

# The function below creates points from a list of coordinates
# Example list: [[-113,23][-120,36][-116,-2]]]

def createPoints(coordinateList, featureClass):

    #import arcpy and create an insert cursor
    import arcpy
    rowInserter = arcpy.InsertCursor(featureClass)

    #Loop through each coordinate in the list
    for coordinate in coordinateList:

        # Grab a set of coordinates from the list and assign them to a point obejct
        x = float(coordinate[0])
        y = float(coordinate[1])
        pointGeometry = arcpy.Point(x,y)

        # use the insert cursor to put in the point object in the feature class
        newPoint = rowInserter.newRow()
        newPoint.Shape = pointGeometry
        rowInserter.insertRow(newPoint)

    # clean up
    del rowInserter
    print "practiceModule1.creatPoints function complete"