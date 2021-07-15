import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
from scipy.io import wavfile

def filterDesign_bandpass(Fth_L, Fth_H, fs):
    f_max = 0.5 * fs
    low_cutoff = Fth_L/f_max
    high_cutoff = Fth_H/f_max
    b, a = butter(5, [low_cutoff, high_cutoff], btype='bandpass')
    return b, a


def bandpass_filter(data,  Fth_L, Fth_H, fs):
    b, a = filterDesign_bandpass( Fth_L, Fth_H, fs)
    y = lfilter(b, a, data)
    return y


Fth_L = 10
Fth_H = 50
Fs, data = wavfile.read('sig1.wav')

y = bandpass_filter(data, Fth_L, Fth_H, Fs)

plt.plot(y)
plt.show()