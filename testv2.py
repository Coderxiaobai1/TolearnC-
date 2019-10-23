""" import numpy as np 
d1 = np.floor(10*np.random.random((2,2)))
print(d1)
d2 = np.floor(10*np.random.random((2,1)))
print(d2)
print(np.hstack((d1,d2)))
a = 35e-3
print(a)
f = 24# mm
H = 5 # m
#pt 转 mm
h_1 = (1743-1546)*2.53*10/72
print(h_1)
h_2 = (2496-2281)*2.53*10/72
print(h_2)
distance_1 = f*H/h_1
distance_2 = f*H/h_2
print(distance_1)
print(distance_2) """
from transformv2 import *
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
B = 117.63662902777779/180*pi
L = 24.470851833333334/180*pi
H = 114.613
a = 6378137#m
b = 6356752#m
e1 = math.sqrt(a*a-b*b)/a
e2 = math.sqrt(a*a-b*b)/b
#N = a/math.sqrt(1-e*e*math.sin(B)*math.sin(B))
alpha = 0
beta = pi/4
distance = 180

m = np.array([[(2919+2980)/2],[1546],[1]])
M_PtoI = PixeltoImage(dx,dy,u0,v0,m)
M_ItoB = ImagetoB(f,M_PtoI)
M_BtoA = BtoA(alpha,beta,M_ItoB)
M_AtoS = AtoS(Phi,Psi,Theta,M_BtoA)
M_StoG = StoG(B,L,H,e1,a,M_AtoS)
print(M_PtoI)
print(M_ItoB)
print(M_BtoA)
print(M_AtoS)
print(M_StoG)

G = CtoG(B,L,H,a,e1)
True_value = CtoG(117.6387256,24/180*pi,24.47122588/180*pi,180,a,e)

#print(M_PtoI)
#print(M_ItoB)
#print(M_BtoA)
#print(M_AtoS)
#print(M_StoG)
print(G)
A_G = Location_IN_G(M_StoG,G,distance)
print(Location_IN_G(M_StoG,G,distance))
G_C = GtoC(A_G,e1,e2,a,b)
print(G_C)