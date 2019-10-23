from pyexiv2 import Image
i = Image('DJI_0294.JPG')
print(i.read_exif())
