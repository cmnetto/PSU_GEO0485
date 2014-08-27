# this script was created for bullet question 2 on exercise 4.1
# A function that takes a path to a feature class as a parameter and returns
#   a Python list of the fields in that feature class. Practice calling the
#   function and printing the list. However, do not print the list within the
#   function.
# https://www.e-education.psu.edu/geog485/node/140

import PE4_1

fc = raw_input("ent the path of your feature class or shapefile:")
print PE4_1.ListFields(fc)