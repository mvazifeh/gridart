import matplotlib.pylab as plt
import numpy as np
import random
from scipy.ndimage import gaussian_filter

mu =9
N = 50
k = 10
eta =10
sigma = 2
p0 = 0.5
inverse_random = False

L = range(N*N)
Q = np.zeros((N*mu,N*mu))
for o in range(mu*mu):
    print(o)
    F = 1000*k
    a = np.ones((N,N))
    for k_ in range(1000):
    
        linear_idx = random.choices(L, weights=a.ravel()/float(a.sum()), k = k)
        x, y = np.unravel_index(linear_idx, a.shape)

        x += np.random.randint(-eta,eta,k)
        y += np.random.randint(-eta,eta,k)
        cond = (x<0) | (x>=N) | (y<0) | (y>=N)
        x_ = np.delete(x, np.where(cond))
        y_ = np.delete(y, np.where(cond))
        a[x_,y_]+=F
        a = gaussian_filter(a,sigma =sigma)
        if np.random.random()>p0 and inverse_random:
            a = a.max()-a
    Mx,My = np.unravel_index(o,(mu,mu))
    Q[Mx*N:(Mx+1)*N,My*N:(My+1)*N] = a

fig,ax = plt.subplots(1,1,figsize = (20,20))
plt.imshow(Q, interpolation='nearest')
plt.axis('off')
