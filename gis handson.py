
import arcpy
import os
from PIL import Image , ExifTags
import random

# ///////////////////hands on 1//////////////////////////////
img_folder=r"D:\8th semester\GIS\Lab\codes\Images"
img_contents = os.listdir(img_folder)

for image in img_contents:
    full_path = os.path.join(img_folder, image)
    pillow_img = Image.open(full_path)
    exif = {ExifTags.TAGS[k]: v for k, v in pillow_img.getexif().items() if k in ExifTags.TAGS}

    if 'GPSInfo' in exif :
      print('gis info exists')
    else:
      print("No GPS data in {}".format(full_path))

# ///////////////////////////hands on 2 ////////////////////////////


shapefile=r"C:\Users\Lenovo\Desktop\gtest\Datasets\ne_10m_admin_0_countries.shp"
arcpy.AddField_management(shapefile, "Favorite", "TEXT")

shp_list = []
with arcpy.da.UpdateCursor(shapefile, ["Favorite"]) as cursor:
    for row in cursor:
      rand = random.randint(0, 1)
      if rand == 0:
          row[0] = "No"
      else :
          row[0] = "Yes"
  
      cursor.updateRow(row)

# ///////////////////////////// hands on 3 ///////////////////////////////

arcpy.env.workspace = r"C:\Users\Lenovo\Desktop\gtest\Datasets"
arcpy.env.overwriteOutput = True

points = r"C:\Users\Lenovo\Desktop\gtest\Datasets\ne_10m_populated_places.shp"
countries = r"C:\Users\Lenovo\Desktop\gtest\Datasets\ne_10m_admin_0_countries.shp"
output = r"C:\Users\Lenovo\Desktop\gtest\output"

arcpy.MakeFeatureLayer_management(points, "Populated_layer" , """ "POP_MAX" < 10000 """)

arcpy.analysis.SpatialJoin(countries,"Populated_layer" , output)
