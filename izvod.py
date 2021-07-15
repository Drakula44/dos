import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile

Fs, data = wavfile.read('sig1.wav')
t = np.linspace(0, np.size(data)/Fs, np.size(data))
izvod = np.diff(data)

plt.plot(izvod)
plt.show()