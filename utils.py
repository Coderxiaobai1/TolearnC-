import numpy as np
import math 
def Rigid_body_transformation(Phi,Psi,Theta,x0,y0,z0):
    """返回刚体变换矩阵 将世界坐标系转化为相机坐标系 * 为对应位置元素相乘 dot为矩阵点乘
    在matlab中*表示矩阵相乘 .*表示矩阵对应位置相乘
    φ=Phi       绕x轴转动的角度
    ψ=Psi       绕y轴转动的角度
    θ=Theta     绕z轴转动的角度
    
    """
    R1 = np.array([[1, 0, 0], [0, math.cos(Phi), math.sin(Phi)], [0, -math.sin(Phi), math.cos(Phi)]],dtype = np.float)
    R2 = np.array([[math.cos(Psi), 0, -math.sin(Psi)], [0, 1, 0], [math.sin(Psi), 0, math.cos(Psi)]],dtype = np.float)
    R3 = np.array([[math.cos(Theta), math.sin(Theta), 0], [-math.sin(Theta), math.cos(Theta), 0], [0, 0, 1]],dtype = np.float)

    #R1 = [1 0 0; 0 cos(Phi) sin(Phi); 0 -sin(Phi) cos(Phi)]
    #R2 = [cos(Psi) 0 -sin(Psi); 0 1 0; sin(Psi) 0 cos(Psi)]
    #R3 = [cos(Theta) -sin(Theta) 0; sin(Theta) cos(Theta) 0; 0 0 1]
    #R = R3*R1*R2
    #此处旋转矩阵的操作得考量一下
    R =np.dot(R3,np.dot(R2,R1))
    #print(R)
    T= np.array([x0, y0, z0],dtype= np.float)
    #
    #打印shape直接shape即可 出现not callable时说明不用括号
    print(T.shape)
    RT1 = np.column_stack((R,T))
    RT = np.row_stack((RT1,np.array([0,0,0,1],dtype = np.float)))
    #RT = [R T; 0 0 0 1]
    return RT
def Projection(f):
    """相机坐标系投影到图像坐标系"""
    #Projection_Matrix = [f 0 0 0; 0 f 0 0; 0 0 1 0]
    Projection_Matrix = np.array([[f, 0, 0, 0], [0, f, 0, 0],[0, 0, 1, 0]],dtype = np.float)
    return Projection_Matrix

def To_Piexl(dx,dy,u0,v0):
    """图像坐标系转化为像素坐标系"""
    nargin = 1
    if nargin ==2:
        u0 = 0
        v0 = 0
    #Pixel_Matrix = [1/dx 0 u0; 0 1/dy v0; 0 0 1]
    Pixel_Matrix = np.array([[1/dx, 0, u0],[0, 1/dy, v0], [0, 0, 1]],dtype = np.float)
    return Pixel_Matrix

def Camera_Parameter():
    #自定义参数
    pi = math.pi
    Phi = pi/4#绕x轴
    Psi = pi/4#绕y轴
    Theta = pi/4#绕z轴
    x0 = 0
    y0 = 0 
    z0 = 0
    f = 35e-3#以米来计算
    dx = 0.026*0.01#一个像素的长 1像素 = 0.635厘米/24 = 0.026458厘米 2.54/72=0.03527 厘米
    dy = 0.026*0.01#一个像素的宽 
    u0 = 0 #图像平面中心
    v0 = 0

    RT = Rigid_body_transformation(Phi,Psi,Theta,x0,y0,z0)
    Projection_Matrix = Projection(f)
    Pixel_Matrix = To_Piexl(dx,dy,u0,v0)
    Camera_Internal_Parameters = np.dot(Pixel_Matrix,Projection_Matrix)
    Camera_External_Parameters = RT
    Camera_Parameters = np.dot(Camera_Internal_Parameters,Camera_External_Parameters)
    print(Camera_Parameters)