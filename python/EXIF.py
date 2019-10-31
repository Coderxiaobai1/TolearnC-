from pyexiv2 import Image

def Process_img(path):
    image = Image(path)
    i_xmp = image.read_xmp()
    info = {
        'GPSLatitude': i_xmp.get('Xmp.drone-dji.GpsLatitude'),
        'GPSLongitude' : i_xmp.get('Xmp.drone-dji.GpsLongtitude'),
        'GPSAltitude': i_xmp.get('Xmp.drone-dji.AbsoluteAltitude'),
        'GPSRelativeAltitude' : i_xmp.get('Xmp.drone-dji.RelativeAltitude'),
        'CameraRoll' : i_xmp.get('Xmp.drone-dji.GimbalRollDegree'),
        'CameraYaw' : i_xmp.get('Xmp.drone-dji.GimbalYawDegree'),
        'CameraPitch' : i_xmp.get('Xmp.drone-dji.GimbalPitchDegree'),
        'FlightRoll' : i_xmp.get('Xmp.drone-dji.FlightRollDegree'),
        'FlightYaw' : i_xmp.get('Xmp.drone-dji.FlightYawDegree'),
        'FlightPitch' : i_xmp.get('Xmp.drone-dji.FlightPitchDegree'),
        'SpeedX' : i_xmp.get('Xmp.drone-dji.FlightXSpeed'),
        'SpeedY' : i_xmp.get('Xmp.drone-dji.FlightYSpeed'),
        'SpeedZ' : i_xmp.get('Xmp.drone-dji.FlightZSpeed'),
        'CalibratedOpticalCenterX' : i_xmp.get('Xmp.drone-dji.CalibratedOpticalCenterX'),
        'CalibratedOpticalCenterY' : i_xmp.get('Xmp.drone-dji.CalibratedOpticalCenterY'),
        'CalibratedOpticalFocalLength' : i_xmp.get('Xmp.drone-dji.CalibratedFocalLength'),

    }
    i_exif = image.read_exif()
    info['XResolution'] = i_exif.get('Exif.Image.XResolution')
    info['YResolution'] = i_exif.get('Exif.Image.YResolution')
    info['PixelXDimension'] = i_exif.get('Exif.Photo.PixelXDimension')
    info['PixelYDimension'] = i_exif.get('Exif.Photo.PixelYDimension')
    info['FocalLength'] = i_exif.get('Exif.Photo.FocalLength')
    info['FocalLengthIn35mmFilm'] = i_exif.get('Exif.Photo.FocalLengthIn35mmFilm')
    return info
info = Process_img('DJI_0298.JPG')
print(info)
print(info['GPSLatitude'])
a = float(info['GPSLatitude'])-100
c = info['XResolution']
b = float(info['XResolution'].split('/',1)[0])
f = float(info['FocalLength'].split('/',1)[0])/100
f1 = float(info['FocalLengthIn35mmFilm'])
print(b)
print(c)
print(f)
print(f1)
