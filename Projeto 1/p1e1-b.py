def step(lowerLimit, upperLimit,impulsePosition):
    begin = np.zeros(impulsePosition-lowerLimit).astype(int)
    end = np.ones(upperLimit-impulsePosition).astype(int)
    
    return np.append(np.append(begin,[1]),end)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,11,1)
y = step(0,10,1) - step(0,10,4)

plt.stem(x,y)
plt.show()



