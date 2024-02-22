import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq, fftshift
import math

t = np.arange(0, 1.2, 0.001)
x = np.sin(2 * np.pi * t)
print(len(x))

plt.plot(t, x)
plt.xlabel("Tid [s]", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)
plt.title("Signal uten hanningvindu")
plt.grid(True)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.show()

han = np.hanning(len(x))
plt.plot(han)
plt.xlabel("Tid [ms]", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)
plt.title("Hanningvindu")
plt.grid(True)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.show()

x_han = x * han
plt.plot(x_han)
plt.xlabel("Tid [ms]", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)
plt.title("Signal med hanningvindu")
plt.tick_params(axis="both", which="major", labelsize=12)
plt.grid(True)
plt.show()


# FFT
N_fft = 2 ** (math.ceil(math.log(len(x), 2)))
x_fft = np.fft.fft(x)
temp_fft = fft(x, N_fft)
temp_fft = 20 * np.log(abs(temp_fft) / np.max(temp_fft))
freq = fftfreq(N_fft, 0.001)
freq = fftshift(freq)
temp_fft = fftshift(temp_fft)

plt.plot(freq, temp_fft)
plt.show()


# FFT hanning
N_fft = 2 ** (math.ceil(math.log(len(x), 2)))
x_fft = np.fft.fft(x_han)
temp_fft = fft(x_han, N_fft)
temp_fft = 20 * np.log(abs(temp_fft) / np.max(temp_fft))
freq = fftfreq(N_fft, 0.001)
freq = fftshift(freq)
temp_fft = fftshift(temp_fft)

plt.plot(freq, temp_fft)
plt.show()
