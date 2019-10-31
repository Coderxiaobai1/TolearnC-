import numpy as np
import matplotlib.pyplot as plt
N = 50 
u , sigma = 92.5, 5
points = sigma*np.random.randn(N,1) + u
x = [x for x in range(1,51)]
plt.figure()
plt.scatter(x,points, c=np.random.rand(N), alpha=0.5)
plt.show()
