import numpy as np
import matplotlib.pyplot as plt
import random

time = np.linspace(0, 5, 500)
signal = np.sin(time)



threshold = 0.7
threshold_array = threshold * np.ones(signal.size)

plt.plot(time, signal)
plt.plot(time, threshold_array)
plt.show()

sum = np.random.uniform(low=-0.1,high=0.1,size=np.size(signal))
signal += sum

plt.plot(time, signal)
plt.plot(time, threshold_array)
plt.show()