#7.1SpatialJoin
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\8th semester\GIS\Lab\codes\Data"

points = r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_populated_places.shp"
countries = r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_admin_0_countries.shp"

output_spatial_join=r"D:\8th semester\GIS\Lab\codes\Outputs\output_feature.shp"

arcpy.SpatialJoin_analysis(countries,points,output_spatial_join)

print ("Done")