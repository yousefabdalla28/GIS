#cities in UAS
import arcpy
data=r"D:\8th semester\GIS\Lab\codes\Data"
output=r"D:\8th semester\GIS\Lab\codes\Outputs"
points=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_populated_places.shp"
countries=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_admin_0_countries.shp"

arcpy.MakeFeatureLayer_management(points,'points_layer')
arcpy.MakeFeatureLayer_management(countries,'countries_layer',""" "NAME"='United States of America' """)

arcpy.SelectLayerByLocation_management('points_layer','WITHIN','countries_layer')
arcpy.FeatureClassToFeatureClass_conversion('points_layer',output,'cities_in_usa')

