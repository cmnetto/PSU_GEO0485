import arcpy

featureClass = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2results\Lesson2PracticeExercise\Lesson2PracticeExercise\USA.gdb\Cities"
fieldList = arcpy.ListFields(featureClass)

for field in fieldList:
    print field.name