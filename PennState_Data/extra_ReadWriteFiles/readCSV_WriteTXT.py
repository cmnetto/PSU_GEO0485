
data = open(r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course" + \
"\PennState_Data\Lesson4results\Proj04_ParsingRhinoSightings\RhinoObservations.csv")
file = open(r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\extra_ReadWriteFiles\newfile.txt", "w")
headerline = data.readline()
headerline = headerline.strip("\n")
valueList = headerline.split(",")

print valueList
s = str(valueList)
file.write(s)

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
    string = str(sighting)
    file.write("\n")
    file.write(string)

    # Create the variables fot the easch column
    RhinoName = sighting[RhinoIndex]
    xCoord = sighting[xIndex]
    yCoord = sighting[yIndex]
    comment = sighting[NoteIndex]
file.close()



