import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile

Fs, data = wavfile.read('sig1.wav')

print(fourier.fft(data))
y = abs(fourier.fft(data))
# y = y[0:np.size(data)//2]
x = np.linspace(0, Fs/2, np.size(data))

plt.plot(x, y)
plt.show()