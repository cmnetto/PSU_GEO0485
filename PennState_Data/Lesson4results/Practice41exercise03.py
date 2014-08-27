# this script was created for bullet question 3 on exercise 4.1
# A function that returns the Euclidean distance between any two coordinates.
#   The coordinates can be supplied as parameters in the form (x1, y1, x2, y2).
#   For example, if your coordinates were (312088, 60271) and (312606, 59468),
#   your function call might look like this: findDistance(312088, 60271, 312606,
#   59468). Use the Pythagorean formula A ** 2 + B ** 2 = C ** 2. For an extra
#   challenge, see if you can handle negative coordinates.
# https://www.e-education.psu.edu/geog485/node/140

import PE4_1
x1 = raw_input("Enter your x1")
y1 = raw_input("Enter your y1")
x2 = raw_input("Enter your x2")
y2 = raw_input("Enter your y2")
print PE4_1.findDistance(float(x1), float(y1), float(x2), float(y2))