#Update cursor
import arcpy
import re
arcpy.env.overwriteOutput=True
arcpy.env.workspace=r"D:\8th semester\GIS\Lab\codes\Data"
output=r"D:\8th semester\GIS\Lab\codes\Outputs"

points=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_populated_places.shp"
countries=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_admin_0_countries.shp"

field_list=arcpy.ListFields(points)
list_fields=[]

for x in field_list:
    print x.name
    print x.type
    if x.type=='String':
        list_fields.append(x.name)
    else:
        print ("this is not string it is a {}".format(x.type))
for filed in list_fields:
    with arcpy.da.UpdateCursor(points,[filed])as city_cursor:
      for x in city_cursor:
        print (x[0])
        if x[0]== ' ':
            x[0]='Updated'
            city_cursor.updateRow(x)
            print ('Value updated to {}'.format(x[0]))

