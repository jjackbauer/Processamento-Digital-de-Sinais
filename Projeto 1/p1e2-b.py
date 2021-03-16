

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
lowerLimit=-8
upperLimit=8

n = np.arange(lowerLimit,upperLimit+1,1)
x = step(lowerLimit,upperLimit,-1)-step(lowerLimit,upperLimit,2)
h = step(lowerLimit,upperLimit,0)-step(lowerLimit,upperLimit,4)

y = convolution(lowerLimit,upperLimit,x,h)

plt.figure()
plt.subplot(311)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.stem(n,x)

plt.subplot(312)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.stem(n,h)


plt.subplot(313)
plt.xlabel('n')
plt.ylabel('x[n]*h[n]')
plt.stem(n,y)
plt.show()


