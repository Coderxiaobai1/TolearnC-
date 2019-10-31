from transformv1 import *
from utils import *
#所需参数
pi = math.pi
Phi = pi/180*5#俯仰角
Psi = pi/180*3#横滚角
Theta = pi/180*4#偏航角
x0 = 0
y0 = 0 
z0 = 0
f = 9e-3#9mm相机转换成m
dx = 0.03527 #cm
dy = 0.03527 
u0 = 5472/2 
v0 = 3648/2
B = 117.63662902777779
L = 24.470851833333334
H = 114.613
a = 6378137#m
b = 6356752#m
e = math.sqrt(a*a-b*b)/a
N = a/math.sqrt(1-e*e*math.sin(B)*math.sin(B))
alpha = 0
beta = pi/4

#测试
Pixel_Matrix = To_Piexl(dx,dy,u0,v0)
Pixel_Matrix_1 = np.linalg.inv(Pixel_Matrix)
M_PtoI = PixeltoImage(dx,dy,u0,v0)
print(M_PtoI)
print(Pixel_Matrix_1)
