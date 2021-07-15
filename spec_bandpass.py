import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile

Fs, data = wavfile.read('sig1.wav')

y = abs(fourier.fft(data))
y = y[0:np.size(data)//2]
x = np.linspace(0, Fs/2, np.size(data)//2)

y1 = y
Fth_L = 10
Fth_H = 100
for i in range(0, np.size(data)//2):
    if (x[i] > Fth_L) and (x[i] < Fth_H):
        y1[i] = y[i]
    else:
        y1[i] = 0

signal = fourier.ifft(y1)

plt.plot(signal)
plt.show()