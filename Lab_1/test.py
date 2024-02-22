import numpy as np
import matplotlib.pyplot as plt

# Definerer signalparametere
Fs = 1000  # Sampling frequency
T = 1 / Fs  # Sampling period
L = 150  # Lengde av signalet
t = np.arange(0, L) * T  # Tidsvektor

# Genererer et signal
f1 = 50  # Frekvenskomponent 1
f2 = 120  # Frekvenskomponent 2
signal = 0.7 * np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# FFT uten zeropadding
N = L  # FFT-lengde er lik signallengden
Y = np.fft.fft(signal, n=N) / L
f = Fs * np.arange(0, (N / 2)) / N

# FFT med zeropadding
Nzp = 1024  # Ny FFT-lengde med zeropadding
Yzp = np.fft.fft(signal, n=Nzp) / L
fzp = Fs * np.arange(0, (Nzp / 2)) / Nzp


# Frekvensdomene
plt.plot(f, 2 * np.abs(Y[0 : N // 2]))
# plt.title("FFT uten Zero-padding")
plt.xlabel("Frekvens (Hz)", fontsize=14)
plt.ylabel("|Y(f)|", fontsize=14)
plt.xlim(0, 200)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.show()


plt.plot(fzp, 2 * np.abs(Yzp[0 : Nzp // 2]))
# plt.title("FFT med Zero-padding")
plt.xlabel("Frekvens (Hz)", fontsize=14)
plt.ylabel("|Y(f)|", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.xlim(0, 200)
plt.show()

# plt.tight_layout()
# plt.show()
