#Cities_In_Egy_Bra
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data"
points = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_admin_0_countries.shp"
output = r"C:\Users\Dell\OneDrive\Desktop\Practical\Outputs"

countries_file = ['Egypt', 'Brazil']
arcpy.MakeFeatureLayer_management(points, 'points_layer')

for x in countries_file:
    print (x)
    arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME"= '{}' """.format(x))
    arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
    arcpy.FeatureClassToFeatureClass_conversion('points_layer', output, 'cities_in_{}'.format(x))
