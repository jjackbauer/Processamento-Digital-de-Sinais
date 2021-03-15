def impulse(lowerLimit, upperLimit,impulsePosition):
    begin = np.zeros(impulsePosition-lowerLimit).astype(int)
    end = np.zeros(upperLimit-impulsePosition).astype(int)
    
    return np.append(np.append(begin,[1]),end)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,11,1)
y = impulse(0,10,3) +impulse(0,10,8)

plt.stem(x,y)
plt.show()



