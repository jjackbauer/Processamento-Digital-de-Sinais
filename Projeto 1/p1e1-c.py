import matplotlib.pyplot as plt
import numpy as np

def senoidal(length, amplitude,frequency,phase):
    x = np.arange(0,length,1)
    return amplitude*np.cos(2*np.pi*frequency*x + np.pi*phase/180)


n = np.arange(0,30,1)
y = senoidal(30,1.5,0.05,90)

plt.stem(n,y)
plt.show()



