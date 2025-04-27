import arcpy
arcpy.env.overwriteOutput=True
arcpy.env.workspace=r"D:\8th semester\GIS\Lab\codes\Data"

points=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_populated_places.shp"
countries=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_admin_0_countries.shp"
output=r"D:\8th semester\GIS\Lab\codes\Outputs"

feature_list=arcpy.ListFeatureClasses()
print (feature_list)
