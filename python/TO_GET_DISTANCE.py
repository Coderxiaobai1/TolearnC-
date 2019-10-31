import numpy as np 
import math
d1 = np.floor(10*np.random.random((2,2)))
print(d1)
d2 = np.floor(10*np.random.random((2,1)))
print(d2)
print(np.hstack((d1,d2)))
a = 35e-3
print(a)
f = 24e-3# m
H = 5 # m原先为5m
#pt 转 mm
#视场角3.093346144273695
print('**********************')
h_1 = (1743-1546)/3648*24*0.001
#h_1 = (2036-1780)*2.53/72*0.01
print(h_1)
h_2 = (2496-2281)*2.53/72*0.01
print(h_2)
distance_1 = f*H/h_1

print('distance')
print(distance_1)
print(math.atan(12/24)/math.pi*180*2)
print(math.atan(18/24)/math.pi*180*2)
print(143/math.sin(20/180*math.pi))