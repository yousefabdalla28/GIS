# 5  Images
from PIL import Image, ExifTags
import os

img_folder = r"C:\Users\Dell\OneDrive\Desktop\Practical\Images"
img_contents = os.listdir(img_folder)


def convert_to_degrees(value):
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)


for image in img_contents:
    full_path = os.path.join(img_folder, image)
    pillow_img = Image.open(full_path)

    exif = {ExifTags.TAGS[k]: v for k, v in pillow_img._getexif().items() if k in ExifTags.TAGS}
    gps_all = {}
    try:
        for key in exif['GPSInfo'].keys():
            print "This is code value {}".format(key)
            decoded_value = ExifTags.GPSTAGS.get(key)
            print "This is its associated lable {}".format(decoded_value)
            gps_all[decoded_value] = exif['GPSInfo'][key]

        long_ref = gps_all.get("GPSLongitudeRef")
        long = gps_all.get("GPSLongitude")
        lat_ref = gps_all.get("GPSLatitudeRef")
        lat = gps_all.get("GPSLatitude")

        if long_ref == "W":
            long_in_degrees = -abs(convert_to_degrees(long))
        else:
            long_in_degrees = convert_to_degrees(long)

        if lat_ref == "S":
            lat_in_degrees = -abs(convert_to_degrees(lat))
        else:
            lat_in_degrees = convert_to_degrees(lat)

        print long_ref, "    ", long_in_degrees
        print lat_ref, "     ", lat_in_degrees

    except:
        print "This image has no GPS info in it {}".format(full_path)
        pass
