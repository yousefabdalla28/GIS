# 7.1SpatialJoin
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data"

points = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_admin_0_countries.shp"
output_spatial_join = r"C:\Users\Dell\OneDrive\Desktop\Practical\output_feature.shp"

arcpy.SpatialJoin_analysis(countries, points, output_spatial_join)

print ("Done")
