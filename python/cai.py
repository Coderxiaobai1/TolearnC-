from pyexiv2 import Image
i = Image('DJI_0294.JPG')
Information = i.read_exif()
for keys, values in Information.items():
    print(keys+':'+values+'\n')
print('*********************')
for keys, values in i.read_xmp().items():
    print(keys+':'+values+'\n')
