# Practice Exercises 4.1

# A function that returns the perimeter of a square given the length of one side.

# Practice Exercise 1
def findPerimeter(side):
    perimeter = side * 4
    return perimeter

# Practice Exercise 2
def ListFields(path):
    import arcpy
    fieldnames = [f.name for f in arcpy.ListFields(path)]
    return fieldnames

# Parctice Exercise 3
def findDistance(x1, y1, x2, y2):
    import math

    distance = math.hypot(x2-x1, y2-y1)
    return distance

