import numpy as np
cechu = np.array([[-2694335.71282456],
 [ 5145773.82618083],
 [ 2625813.22279317]])
zhenshi = np.array([[-2694619.92770917],
 [ 5145858.40536698],
 [ 2625951.27411924]])
wurenji = np.array([[-2694411.98329207],
 [ 5145919.4848881 ],
 [ 2625886.47821469]])
print('Error:')
print(zhenshi-cechu)
print(zhenshi-wurenji)