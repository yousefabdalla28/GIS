# cities in UAS
import arcpy

arcpy.env.workspace = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data"
points = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_admin_0_countries.shp"
output = r"C:\Users\Dell\OneDrive\Desktop\Practical\Outputs"

arcpy.MakeFeatureLayer_management(points, 'points_layer')
arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME"='United States of America' """)

arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
arcpy.FeatureClassToFeatureClass_conversion('points_layer', output, 'cities_in_usa')
