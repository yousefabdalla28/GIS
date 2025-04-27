# Search Cursor
import arcpy

data=r"D:\8th semester\GIS\Lab\codes\Data"
output=r"D:\8th semester\GIS\Lab\codes\Outputs"
points=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_populated_places.shp"
countries=r"D:\8th semester\GIS\Lab\codes\Data\ne_10m_admin_0_countries.shp"

cities_cursor = arcpy.SearchCursor(points,['NAME','POP_MAX','TIMEZONE'])

for x in cities_cursor:
    print(x.getValue('NAME'))
    print(x.getValue('POP_MAX'))
    print(x.getValue('TIMEZONE')) +"\n"