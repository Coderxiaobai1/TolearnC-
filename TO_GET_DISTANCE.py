import numpy as np 
d1 = np.floor(10*np.random.random((2,2)))
print(d1)
d2 = np.floor(10*np.random.random((2,1)))
print(d2)
print(np.hstack((d1,d2)))
a = 35e-3
print(a)
f = 9e-3# mm
H = 5 # m
#pt 转 mm
print('**********************')
h_1 = (1743-1546)*2.53/72*0.01
print(h_1)
h_2 = (2496-2281)*2.53/72*0.01
print(h_2)
distance_1 = f*H/h_1
distance_2 = f*H/h_2
print(distance_1)
print(distance_2)