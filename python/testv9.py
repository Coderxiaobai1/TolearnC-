# 把角度改为非绝对值
from transformv5 import *
import matplotlib.pyplot as plt
def ALL(path,m,distance):
    '''path 图像位置，m为所求出的框的像素点为3行1列'''
    info = Process_img(path)
    f = float(info['FocalLengthIn35mmFilm'].split('/',1)[0])/100/1000
    #print(f)
    #print(info['FocalLength'])
    Phi = PI/180*float(info['FlightPitch'])
    Psi = PI/180*float(info['FlightYaw'])
    Theta = PI/180*float(info['FlightRoll'])
    alpha = PI/180*float(info['CameraYaw'])
    beta = PI/180*float(info['CameraPitch'])
    dx = 2.56/float(info['XResolution'].split('/',1)[0])*0.01
    dy = 2.56/float(info['YResolution'].split('/',1)[0])*0.01
    u0 = float(info['CalibratedOpticalCenterX'])
    v0 = float(info['CalibratedOpticalCenterY'])
    B = float(info['GPSLongitude'])/180*PI
    L = float(info['GPSLatitude'])/180*PI
    H = float(info['GPSAltitude'])
    a = 6378137
    b = 6356752
    e1 = math.sqrt(a*a-b*b)/a
    e2 = math.sqrt(a*a-b*b)/b
    distance = distance 
    M_PtoI = PixeltoImage(dx,dy,u0,v0,m)
    M_ItoB = ImagetoB(f,M_PtoI)
    M_BtoA = BtoA(alpha,beta,M_ItoB)
    M_AtoS = AtoS(Phi,Psi,Theta,M_BtoA)
    M_StoG = StoG(B,L,H,e1,a,M_AtoS)
    G = CtoG(B,L,H,a,e1)
    A_G = Location_IN_G(M_StoG,G,distance)
    G_C = GtoC(A_G,e1,e2,a,b)

    #print('object in G：\n')
    #print(A_G)
    True_value_G = CtoG(117.6387256/180*PI,24.47122588/180*PI,50,a,e1)
    #print('True_value_G:\n')
    #print(True_value_G)
    #print('Error:')
    #print(A_G-True_value_G)

    return G_C, info
m = np.array([[(2919+2980)/2.0000000],[1546.0000000],[1.0000000]],dtype=np.float_)#原先设置的为杆塔顶点
#m = np.array([[(2919+2980)/2.0000000],[(1546+1743)/2],[1.0000000]],dtype=np.float_)#现在设置为杆塔中点

N = 50 
#u , sigma = 92.5, 10 第一次距离H=5推出距离92.5
u, sigma = 92.58883248730965,20

a = 6378137
b = 6356752
e1 = math.sqrt(a*a-b*b)/a
e2 = math.sqrt(a*a-b*b)/b
points = u - sigma*np.random.rand(N,1)
print(points)
aver = np.zeros((3,1))
print(aver)

for i in points:
    #aver = aver + ALL('DJI_0294.JPG',m,i)
    shoot, info = ALL('DJI_0294.JPG',m,i)
    print(shoot)
print(info)
#output = aver/50  
#print(output[0])
#print(output[1])
#print(output[2])
#cechu = CtoG(output[0]/180*PI,output[1]/180*PI,output[2],a,e1)
#shiji = CtoG(117.6387256/180*PI,24.47122588/180*PI,output[2],a,e1)
#print(GtoC(shiji,e1,e2,a,b))
#print(output)
#print(cechu-shiji)