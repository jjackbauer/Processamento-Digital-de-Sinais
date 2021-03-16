

def step(lowerLimit, upperLimit,impulsePosition):
    begin = np.zeros(impulsePosition-lowerLimit)
    end = np.ones(upperLimit-impulsePosition)
    
    return np.append(np.append(begin,[1]),end)

def convolution(lowerLimit,upperLimit,x,h):
    response = np.zeros(upperLimit-lowerLimit+1)

    for n in range(lowerLimit,upperLimit+1):
        for k in range(lowerLimit,upperLimit+1):
            response[n] += x[k]*h[n-k]

    return response

import matplotlib.pyplot as plt
import numpy as np
from  scipy import signal

lowerLimit=-10
upperLimit=10

n = np.arange(lowerLimit,upperLimit+1,1)
x = step(lowerLimit,upperLimit,0)-step(lowerLimit,upperLimit,8)
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
plt.stem(n,y)


plt.subplot(414)
plt.xlabel('n')
plt.ylabel('x[n]*h[n] - scipy')
plt.stem(y1)
plt.show()


