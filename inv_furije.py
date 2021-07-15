import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile

Fs, data = wavfile.read('sig1.wav')

y = abs(fourier.fft(data))
y = y[0:np.size(data)//2]
x = np.linspace(0, Fs/2, np.size(data)//2)

y1 = y
Ath = 5600000
for i in range(0, np.size(data)//2):
    if y[i] < Ath:
        y1[i] = 0
    else:
        y1[i] = y[i]

signal = fourier.ifft(y1);

plt.plot(signal)
plt.show()