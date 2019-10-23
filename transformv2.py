import numpy as np 
import math
PI = math.pi
def PixeltoImage(dx,dy,u0,v0,m):
    Pixel_Matrix = np.array([[dx, 0, -u0*dx],[0, dy, -v0*dy],[0, 0, 1]])
    return np.dot(Pixel_Matrix,m)
    #return Pixel_Matrix

def ImagetoB(f,m):
    return np.array([[m[0][0]],[m[1][0]],[-f],[1]])

def BtoA(alpha,beta,m):
    '''将摄像机坐标系转化到无人机载机坐标系'''
    M1 = np.array([[math.cos(alpha), 0, math.sin(alpha), 0],[0, 1, 0, 0],
    [-math.sin(alpha), 0, math.cos(alpha), 0],[0, 0, 0, 1]])
    M2 = np.array([[1, 0, 0, 0],[0, math.cos(beta), -math.sin(beta), 0],
    [0, -math.sin(beta), math.cos(beta), 0],[0, 0, 0, 1]])
    return np.dot(np.dot(M1,M2),m)
def AtoS(Phi,Psi,Theta,m):
    """返回刚体变换矩阵 将世界坐标系转化为相机坐标系 * 为对应位置元素相乘 dot为矩阵点乘
    在matlab中*表示矩阵相乘 .*表示矩阵对应位置相乘
    φ=Phi       绕x轴转动的角度
    ψ=Psi       绕y轴转动的角度
    θ=Theta     绕z轴转动的角度
    """
    R_x = np.array([[1, 0, 0, 0],[0, math.cos(Phi), math.sin(Phi), 0],
    [0, -math.sin(Phi), math.cos(Phi), 0],[0, 0, 0, 1]])
    R_y = np.array([[math.cos(Psi), 0, -math.sin(Psi), 0],[0, 1, 0, 0],
    [math.sin(Psi), 0, math.cos(Psi), 0],[0, 0, 0, 1]])
    R_z = np.array([[math.cos(Theta), math.sin(Theta), 0, 0],[-math.sin(Theta), math.cos(Theta), 0, 0],
    [0, 0, 1, 0],[0, 0, 0, 1]])
    R_all = np.dot(R_x, np.dot(R_y, R_z))
    return np.dot(R_all,m)

def StoG(B,L,H,e,a,m):
    ''''''
    N = a/math.sqrt(1-e*e*math.sin(B)*math.sin(B))
    M6 = np.array([[1, 0, 0, 0],[0, 1, 0, 0],
    [0, 0, 1, N*e*e*math.sin(B)],[0, 0, 0, 1]])
    M7 = np.array([[math.cos(L), -math.sin(L), 0, 0],[math.sin(L), math.cos(L), 0, 0],
    [0, 0, 1, 0],[0, 0, 0, 1]])
    M8 = np.array([[math.cos(-L), 0, math.sin(-L), 0],[0, 1, 0, 0],
    [-math.sin(-L), 0, math.cos(-L), 0],[0, 0, 0, 1]])
    M9 = np.array([[1, 0, 0, H],[0, 1, 0, 0],
    [0, 0, 1, 0],[0, 0, 0, 1]])
    M_all = np.dot(M6,np.dot(M7,np.dot(M8,M9)))
    return np.dot(M_all,m)

def CtoG(B,L,H,a,e):
    '''大地直角坐标系转换为空间直角坐标系下的坐标值'''
    N = a/math.sqrt(1-e*e*math.sin(B)*math.sin(B))
    x = (N+H)*math.cos(B)*math.cos(L)
    y = (N+H)*math.cos(B)*math.sin(L)
    z = N*((1-e*e)+H)*math.sin(B)
    return np.array([[x],[y],[z]])

def Location_IN_G(a,S,distance):
    d = 0
    for i in range(3):
        #print(i)
        #print(a[i][0])
        #print(S[i][0])
        d = d + math.pow(a[i][0]-S[i][0],2)
    X_A = math.sqrt(math.pow(distance,2)/d)*(a[0][0]-S[0][0]) + S[0][0]
    Y_A = math.sqrt(math.pow(distance,2)/d)*(a[1][0]-S[1][0]) + S[1][0]
    Z_A = math.sqrt(math.pow(distance,2)/d)*(a[2][0]-S[2][0]) + S[2][0]
    return np.array([[X_A],[Y_A],[Z_A]])

def GtoC(A_G,e1,e2,a,b,):
    '''这里直接用直接法好了'''
    U = math.atan(A_G[2][0]*a/(math.sqrt(math.pow(A_G[0][0],2)+math.pow(A_G[1][0],2))*b))
    B = math.atan((A_G[2][0]+b*math.pow(e2,2)*math.pow(math.sin(U),3))/
    (math.sqrt(math.pow(A_G[0][0],2)+math.pow(A_G[1][0],2))-a*e1*e1*math.pow(math.cos(U),3)))
    L = math.atan(A_G[1][0]/A_G[0][0])
    N = a/math.sqrt(1-e1*e1*math.sin(B)*math.sin(B))
   
    H = math.sqrt(math.pow(A_G[0][0],2)+math.pow(A_G[1][0],2))/math.cos(B) - N
    B = B*180/PI
    L = L*180/PI
    shoot = math.atan(1)
    return np.array([[B],[L],[H],[shoot]])