# Count countries within range
import arcpy
arcpy.env.overwriteOutput=True

data=r"D:\8th semester\GIS\Lab\codes\Data"
output=r"D:\8th semester\GIS\Lab\codes\Outputs"

points=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_populated_places.shp"
countries=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_admin_0_countries.shp"
total_count=0
created_count=0

arcpy.MakeFeatureLayer_management(points,'points_layer')
country_cursor=arcpy.SearchCursor(countries,['FID','SOVEREIGNT','POP_EST'])
for x in country_cursor:
    total_count+=1
    if x.getValue('POP_EST')>50000000:
        created_count+=1
        name= str(x.getValue('SOVEREIGNT')).replace('(','').replace(')','').replace(' ','_').replace('-','_')
        print name.format(name.encode('utf-8'))
        print x.getValue('POP_EST')
        arcpy.MakeFeatureLayer_management(countries,'countries_layer',""" "FID"={} """.format(x.getValue('FID')))
        arcpy.SelectLayerByLocation_management('points_layer','WITHIN','countries_layer')
        arcpy.FeatureClassToFeatureClass_conversion('points_layer',output,"CityIn{0}{1}".format(name,x.getValue('FID')))
    else:
        print"{} didn't meet the criteria".format(name)

print 'Finished'
print('{} met the criteria out of {} countries'.format(created_count, total_count))
