# Feature List
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data"

points = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_admin_0_countries.shp"
output = r"C:\Users\Dell\OneDrive\Desktop\Practical\Outputs"

feature_list = arcpy.ListFeatureClasses()
print (feature_list)
