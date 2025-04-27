#Update cursor
import arcpy
import re
arcpy.env.overwriteOutput=True
arcpy.env.workspace=r"D:\8th semester\GIS\Lab\codes\Data"
output=r"D:\8th semester\GIS\Lab\codes\Outputs"

points=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_populated_places.shp"
countries=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_admin_0_countries.shp"

field_list=arcpy.ListFields(points)
list_field=[]

for x in field_list:
    print x.name
    print x.type
    if x.type=='String':
        list_field.append(x.name)
    else:
        print "this is not string , it is a {}".format(x.type)
for field in list_field:
    updateCursor=arcpy.UpdateCursor(points,[field])
    for row in updateCursor:
        print row.getValue('NAME')
        if row.getValue('NAME')== ' ':
            row.NAME='Updated'
            updateCursor.updateRow(row)
            print 'value updated to {}'.format(row.getValue('NAME'))