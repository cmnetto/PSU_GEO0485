import arcpy

fc = r"\\imsnolna04\nettoc\My Documents\Python_Learning\PSU_ArcPy_course\PennState_Data\Lesson2results\Lesson2PracticeExercise\Lesson2PracticeExercise\USA.gdb\Cities"

rows = arcpy.SearchCursor(fc)
row = rows.next()

while row:
    print row.NAME
    row = rows.next()