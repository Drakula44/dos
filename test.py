import numpy as np
import matplotlib.pyplot as plt

data = np.fromfile('ECG.dat', dtype = int)
signal=np.diff(data)
plt.plot(signal)
plt.show()
br = 0
i = 0
while i<np.size(signal)-1:
    if signal[i] > 500000:
        br = br+1
        i = i + 100
    else:
        i = i + 1
print(br)