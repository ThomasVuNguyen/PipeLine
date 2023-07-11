"""Calculates total volume of all walls in the model."""

from Autodesk.Revit import DB

doc = __revit__.ActiveUIDocument.Document

# Create a collector instatance and collect volume data
wall_collector = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

# Iterate over wall and collect Volume data
total_volume = 0.0

for wall in wall_collector:
    vol_param = wall.Parameter[DB.BuiltInParameter.HOST_VOLUME_COMPUTED]
    if vol_param:
        total_volume = total_volume + vol_param.AsDouble()
        
print("Total volume is: {}".format(total_volume))