# 4.2 4.2 Reading and parsing text

# Read a GPS produced text file and write the lat and long values to a list
# of coordinates
gpstrack = open(r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson4results\gps_track.txt", "r")

# figure out position of the lat and long in the header
headerLine = gpstrack.readline()
valueList = headerLine.split(",")

latValueIndex = valueList.index("lat")
lonValueIndex = valueList.index("long")

# Read line in the file and append to coordinate list
coordList = []

for line in gpstrack.readlines():
    # need to say what the seperating value is, in this case its the ","
    segmentedLine = line.split(",")
    # only append the value (index) indicated... we could have used "segmentedline[2]", but if lat changes position in the header list
    # we would have to change the index number.
    coordList.append([segmentedLine[lonValueIndex], segmentedLine[latValueIndex]])

print coordList