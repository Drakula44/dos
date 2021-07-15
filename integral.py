import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile

Fs, data = wavfile.read('sig1.wav')
t = np.linspace(0, np.size(data)/Fs, np.size(data))
integral = np.zeros(np.size(data))

for i in range(2, np.size(data)):
    integral[i] = integral[i-1] + data[i]*1/Fs

plt.plot(t, integral)
plt.show()

