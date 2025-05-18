#7.2Buffer_Clip
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\8th semester\GIS\Lab\codes\Data"

points = r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_populated_places.shp"
cities_in_egypt = r"D:\8th semester\GIS\Lab\codes\Data\cities_in_Egypt.shp"

output_feature = r"D:\8th semester\GIS\Lab\codes\Outputs\output_feature.shp"
arcpy.Buffer_analysis(cities_in_egypt, output_feature, '10 Kilometers')

output_road_clip=r"D:\8th semester\GIS\Lab\codes\Outputs\cities_in_egypt_clipped.shp"
arcpy.Clip_analysis(points,cities_in_egypt,output_road_clip)

print ("Done")