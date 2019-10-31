from transformv5 import *
pi = math.pi
Phi = pi/180*4.9#俯仰角
print(Phi)
Psi = pi/180*(-6.6)#横滚角
Theta = pi/180*79.6#偏航角
x0 = 0
y0 = 0 
z0 = 0
f = 9e-3#9mm相机转换成m
dx = 0.03527*0.01 #m
dy = 0.03527*0.01#m
u0 = 5472/2 
v0 = 3648/2
B = 117.63662902777779/180*pi#经度
print(B)
L = 24.470851833333334/180*pi#纬度
H = 114.613
a = 6378137#m
b = 6356752#m
e1 = math.sqrt(a*a-b*b)/a
print(e1)
e2 = math.sqrt(a*a-b*b)/b
print(e2)
#N = a/math.sqrt(1-e*e*math.sin(B)*math.sin(B))
alpha = pi/180*(-22.6)
beta = pi/180*77.9
distance = 180

m = np.array([[(2919+2980)/2.0000000],[1546.0000000],[1.0000000]],dtype=np.float_)
print(m)
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
print('*************************')
G = CtoG(B,L,H,a,e1)
True_value_G = CtoG(117.6387256/180*pi,24.47122588/180*pi,180,a,e1)
print('True_value_G:\n')
print(True_value_G)
True_value_C = GtoC(True_value_G,e1,e2,a,b)
print('True_value_C:\n')
print(True_value_C)

T = np.array([[117.6387256],[24.47122588],[180]])

#print(M_PtoI)
#print(M_ItoB)
#print(M_BtoA)
#print(M_AtoS)
#print(M_StoG)
print('无人机坐标:\n')
print(G)
A_G = Location_IN_G(M_StoG,G,distance)
print('object in G：\n')
print(A_G)
G_C = GtoC(A_G,e1,e2,a,b)
print('True object in C:\n')
print(T)
print('Inherence in C：\n')
print(G_C)