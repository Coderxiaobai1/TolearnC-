from utils import *
pi = math.pi
Phi = pi/4
Psi = pi/4
Theta = pi/4
x0 = 0
y0 = 0 
z0 = 0
f = 9e-3#9mm相机转换成m
dx = 0.03527 #cm
dy = 0.03527 
u0 = 0 
v0 = 0

RT = Rigid_body_transformation(Phi,Psi,Theta,x0,y0,z0)
Projection_Matrix = Projection(f)
Pixel_Matrix = To_Piexl(dx,dy,u0,v0)

Camera_Internal_Parameters = np.dot(Pixel_Matrix,Projection_Matrix)
Camera_External_Parameters = RT
Camera_Parameters = np.dot(Camera_Internal_Parameters,Camera_External_Parameters)
print(Camera_External_Parameters)
print(Camera_Internal_Parameters)
print(Camera_Parameters)
"""
CCD尺寸为h*v
水平、垂直方向的视场角为：theta_h = 2*math.arctan(h/(2*f))
theta_v = 2* math.arctan(v/(2*f))
分辨率表示在水平和垂直上显示的每英寸点的数量。
CCD靶面尺寸指的是CCD传感器的感光部分的大小，一般用英寸表示。1 inch = 2.54cm


"""