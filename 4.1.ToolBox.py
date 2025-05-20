# ToolBox
import arcpy
import re

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data"

points = arcpy.GetParameterAsText(0)
countries = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2)
pop_number = arcpy.GetParameterAsText(3)

total_count = 0
created_count = 0
# with arcpy.SearchCursor(countries,'FID','SOVEREIGNT','POP_EST']) as country_cursor
arcpy.MakeFeatureLayer_management(points, 'points_layer')
country_cursor = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'POP_EST'])
for x in country_cursor:
    total_count += 1
    if x.getValue('POP_EST') > float(pop_number):
        created_count += 1
        name = str(x.getValue('SOVEREIGNT')).replace('(', '').replace(')', '').replace(' ', '_').replace('-', '_')
        print name.format(name.encode('utf-8'))
        print x.getValue('POP_EST')
        arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID"={} """.format(x.getValue('FID')))
        arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
        arcpy.FeatureClassToFeatureClass_conversion('points_layer', output,
                                                    "CityIn{0}{1}".format(name, x.getValue('FID')))
        arcpy.AddMessage("Success")
    else:
        print"{} didn't meet the criteria".format(name)

print ('Finished')
print('{} met the criteria out of {} countries'.format(created_count, total_count))
