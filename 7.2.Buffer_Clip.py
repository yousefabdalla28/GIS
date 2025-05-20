# 7.2Buffer_Clip
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data"

points = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_admin_0_countries.shp"
cities_in_egypt = r"C:\Users\Dell\OneDrive\Desktop\Practical\Outputs\cities_in_Egypt.shp"

output_feature = r"C:\Users\Dell\OneDrive\Desktop\Practical\Outputs\output_feature.shp"
arcpy.Buffer_analysis(cities_in_egypt, output_feature, '10 Kilometers')

output_road_clip = r"C:\Users\Dell\OneDrive\Desktop\Practical\Outputs\cities_in_egypt_clipped.shp"
arcpy.Clip_analysis(points, cities_in_egypt, output_road_clip)

print ("Done")
