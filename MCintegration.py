import numpy as np
import math as m
import matplotlib.pyplot as plt

def f(x):
    return (np.cos(50*x)+np.sin(20*x))**2


def h(x):
    return 1


def mc_integration(a,b,N,f,h):
    N = int(N)
    summe = 0
    progress = []
    x_values = np.random.uniform(a,b,N)

    for i in range(N):
        summe = summe + f(x_values[i])
        progress.append(summe/(i+1))
        #print(i,summe/(i+1))

    return progress

N = 1e6

progress = np.asarray(mc_integration(0,1,N,f,h))

steps = np.arange(1,N+1)

print(progress[-1])
plt.plot(np.log(steps),progress)
plt.axis([0,np.log(N),0.7,1.05])
plt.show() 
