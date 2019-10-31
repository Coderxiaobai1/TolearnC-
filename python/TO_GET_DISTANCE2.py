import numpy as np 
import math
f = 24e-3# m
H = 5 # m
#pt 转 mm
print('**********************')
h_1 = (1743-1546)/3648*24*0.001
#h_1 = (2036-1780)*2.53/72*0.01
print(h_1)
jiaodu = math.atan(h_1/2/f)
print(jiaodu/math.pi*180*2)#3.093346144273695视场角
distance2 = 2.5/math.tan(jiaodu)
print(distance2)
h_2 = (2496-2281)*2.53/72*0.01
print(h_2)
distance_1 = f*H/h_1

print('distance')
print(distance_1)
print(math.atan(12/24)/math.pi*180*2)
print(math.atan(18/24)/math.pi*180*2)