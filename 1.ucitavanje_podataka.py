import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import matplotlib.pyplot as plt


Fs, data = wavfile.read('sig1.wav')

print("Frekvencija odabiranja: {} Hz".format(Fs))
print("Veličina ulaznog signala: {}".format(data.size))

time = np.linspace(0, data.size//Fs, data.size)

plt.plot(time, data)
plt.title("sig1.wav")
plt.xlabel("Vreme [s]")
plt.ylabel("Amplituda [?]")
plt.show()

x = np.fromfile('EMG.dat', dtype=int)

plt.plot(x)
plt.show()