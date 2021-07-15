import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
from scipy.io import wavfile

def filterDesign_lowpass(cutoff, fs):
    f_max = 0.5 * fs
    normal_cutoff = cutoff / f_max
    b, a = butter(5, normal_cutoff, btype='low')
    return b, a


def lowpass_filter(data, f_th, fs):
    b, a = filterDesign_lowpass(f_th, fs)
    y = lfilter(b, a, data)
    return y


Fth = 10
Fs, data = wavfile.read('sig1.wav')

y = lowpass_filter(data, Fth, Fs)

plt.plot(y)
plt.show()