


import os
file = open(r"M:\Work\nettoc\MAS201400151_PSU\data\PennState_Data\extra_ReadWriteFiles/TurnInDir.txt", "w")
for root, dirs, files in os.walk(r"M:\Work\nettoc\MAS201400151_PSU\data"):
    for f in files:
##        if f.endswith(".docx"):  # use this to specify the file type
            print os.path.join(root, f)
            s = (os.path.join(root, f))
            file.write(s)
            file.write("\n")
file.close()

