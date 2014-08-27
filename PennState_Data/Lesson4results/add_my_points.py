# This script is saved as add_my_points.py

# Import the module containing a function we want to call
import practiceModule1

# Define point list and shapefile to edit
myWorldLocations =  [[-123.9,47.0],[-118.2,34.1],[-112.7,40.2],[-63.2,-38.7]]
myWorldFeatureClass = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson4results\WorldPoints.shp"

# Call the createPoints function from practiceModule1
practiceModule1.createPoints(myWorldLocations, myWorldFeatureClass)

print"complete"