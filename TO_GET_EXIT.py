import exifread
# http://www.sharejs.com
# Open image file for reading (binary mode)
def Process_img(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    info = {
        'Image DateTime': tags.get('Image DateTime', '0').values,
        'GPS GPSLatitudeRef(纬度标志)': tags.get('GPS GPSLatitudeRef', '0').values,
        'GPS GPSlatitude(纬度)': tags.get('GPS GPSLatitude', '0').values,
        'GPS GPSLongitudeRef(经度标志)': tags.get('GPS GPSLongitudeRef', '0').values,
        'GPS GPSLongitude(经度标志)': tags.get('GPS GPSLongitude', '0').values,
        'Image XResolution': tags.get('Image XResolution', '0').values,
        'Image YResolution': tags.get('Image YResolution', '0').values,
        'Exif ExifImageWidth': tags.get('EXIF ExifImageWidth', '0').values,
        'EXIF EXIFImageLength': tags.get('EXIF ExifImageLength', '0').values,

    }
    return info
info = Process_img('DJI_0298.JPG')
print(info)