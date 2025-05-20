# Select with Search Cursor
import arcpy
import re

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data"
points = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_admin_0_countries.shp"
output = r"C:\Users\Dell\OneDrive\Desktop\Practical\Outputs"

arcpy.MakeFeatureLayer_management(points, 'points_layer')
country_cursor = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT'])
for x in country_cursor:
    name = str(x.getValue('SOVEREIGNT')).replace('(', '').replace(')', '').replace('-', '_')
    print (name)
    arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID"={} """.format(x.getValue('FID')))
    arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
    arcpy.FeatureClassToFeatureClass_conversion('points_layer', output, "cityIn{0}{1}".format(name, x.getValue('FID')))
