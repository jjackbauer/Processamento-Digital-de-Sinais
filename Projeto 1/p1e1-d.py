def exponential(length, k,c):
    x = np.arange(0,length,1)
    return k*np.exp(c*x)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,30,1)
y = exponential(30,1,1/12+(np.pi/6)*1j)


plt.figure()
plt.subplot(211)
plt.xlabel('Sample')
plt.ylabel('Magnitude')
plt.stem(x,np.real(y))

plt.subplot(212)
plt.xlabel('Sample')
plt.ylabel('Phase')
plt.stem(x,np.imag(y))
plt.show()



