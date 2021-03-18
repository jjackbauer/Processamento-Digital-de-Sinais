

def step(lowerLimit, upperLimit,impulsePosition):
    begin = np.zeros(impulsePosition-lowerLimit)
    end = np.ones(upperLimit-impulsePosition)
    
    return np.append(np.append(begin,[1]),end)

def convolution(lowerLimit,upperLimit,x,h):
    size = upperLimit-lowerLimit
    response = np.zeros(2*size+1)
    anexx = np.zeros(int(size/2))
    xCopy = x
    hCopy = h

    xCopy= np.append(np.append(anexx,xCopy),anexx)
    hCopy= np.append(np.append(anexx,hCopy),anexx)

    for n in range(0,size):
        for k in range(0,2*size):
            response[n+size] += xCopy[k]*hCopy[n-k]

    return response

import matplotlib.pyplot as plt
import numpy as np
from  scipy import signal

lowerLimit=-10
upperLimit=10

n = np.arange(lowerLimit,upperLimit+1,1)
x = step(lowerLimit,upperLimit,-1)-step(lowerLimit,upperLimit,2)
h = step(lowerLimit,upperLimit,0)-step(lowerLimit,upperLimit,4)

y = convolution(lowerLimit,upperLimit,x,h)
y1 = signal.convolve(x,h)

plt.figure()
plt.subplot(411)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.stem(n,x)

plt.subplot(412)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.stem(n,h)


plt.subplot(413)
plt.xlabel('n')
plt.ylabel('x[n]*h[n]')
n1 = np.arange(-y.size/2,y.size/2,1)
plt.stem(n1,y)


plt.subplot(414)
plt.xlabel('n')
plt.ylabel('x[n]*h[n] - scipy')
n2 = np.arange(-(y1.size/2),y1.size/2,1)
plt.stem(n2,y1)
plt.show()


