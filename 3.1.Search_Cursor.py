# Search Cursor
import arcpy

arcpy.env.workspace = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data"
points = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\Dell\OneDrive\Desktop\Practical\Data\ne_10m_admin_0_countries.shp"
output = r"C:\Users\Dell\OneDrive\Desktop\Practical\Outputs"

cities_cursor = arcpy.SearchCursor(points, ['NAME', 'POP_MAX', 'TIMEZONE'])

for x in cities_cursor:
    print(x.getValue('NAME'))
    print(x.getValue('POP_MAX'))
    print(x.getValue('TIMEZONE')) + "\n"
