import numpy as np 
import math
def PixeltoImage(dx,dy,u0,v0):
    Pixel_Matrix = np.array([[dx, 0, -u0*dx],[0, dy, -v0*dy],[0, 0, 1]])
    return Pixel_Matrix

def ImagetoB(m,f):
    return np.row_stack((m,np.array([[-f],[1]])))
def BtoA(alpha,beta):
    '''将摄像机坐标系转化到无人机载机坐标系'''
    M1 = np.array([[math.cos(alpha), 0, math.sin(alpha), 0],[0, 1, 0, 0],
    [-math.sin(alpha), 0, math.cos(alpha), 0],[0, 0, 0, 1]])
    M2 = np.array([[1, 0, 0, 0],[0, math.cos(beta), -math.sin(beta), 0],
    [0, -math.sin(beta), math.cos(beta), 0],[0, 0, 0, 1]])
    return np.dot(M1,M2)
def AtoS(Phi,Psi,Theta):
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
    return np.dot(R_x, np.dot(R_y, R_z))

def StoG(B,L,H,N,e):
    ''''''
    M6 = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],
    [0, 0, 1, 0],[0, 0, N*e*e*math.sin(B), 1]])
    M7 = np.array([[math.cos(L), -math.sin(L), 0, 0],[math.sin(L), math.cos(L), 0, 0],
    [0, 0, 1, 0],[0, 0, 0, 1]])
    M8 = np.array([[math.cos(-L), 0, math.sin(-L), 0],[0, 1, 0, 0],
    [-math.sin(-L), 0, math.cos(-L), 0],[0, 0, 0, 1]])
    M9 = np.array([[1, 0, 0, H],[0, 1, 0, 0],
    [0, 0, 1, 0],[0, 0, 0, 1]])
    return np.dot(M6,np.dot(M7,np.dot(M8,M9)))

def CtoG(B,L,H,N,e):
    '''返回空间直角坐标系下的坐标值'''
    x = (N+H)*math.cos(B)*math.cos(L)
    y = (N+H)*math.cos(B)*math.sin(L)
    z = N*((1-e*e)+H)*math.sin(B)
    return np.array([[x],[y],[z]])

