from plot_bin import *
from plot_data import *
from raspi_import import raspi_import
from fft_converter import *
import os
import numpy as np
import scipy.signal as sig
import pandas as pd


bin_filenames = os.listdir("./bin_files")
print("Files to plot:")
for i in range(0, len(bin_filenames)):
    print(str(i) + ": " + bin_filenames[i])

filepath_number = int(input("Choose file to plot: "))

filepath_relative = "./bin_files/" + bin_filenames[filepath_number]


sample_period, data = raspi_import(filepath_relative)
data = sig.detrend(data[5:], axis=0)
data = np.transpose(data)

skalerings_faktor = 0.0008058608
data *= skalerings_faktor

x_axis = []
if isinstance(sample_period, (int, float)):
    dt = sample_period
    x_axis = np.arange(0, len(data[0]) * dt, dt)
    x_axis = [x_axis] * len(data)

# print(sample_period)

# plot_offset(sample_period, data, "Tid [s]", "Spenning [V]")
# plot_data_together(data, sample_period)
# plot_data_subplot_len(sample_period, data, len(data), "Tid [s]", "Spennning [V]")

# plot_data_single(x_axis[1], data[1], "Tid [s]", "Spennning[V]", 0, 10 / 200)
# plot_data_single(x_axis[0], data[0], "Tid [s]", "Spennning[V]", 0, 0.05)


# FFT plots

fft_data, freq_data = data_fft_converter(data, sample_period)

data = hanning_window(data)
fft_data_hanning, freq_data_hanning = data_fft_converter(data, sample_period)
# fft_data_hanning, freq_data_hanning = zero_padding_data_fft_converter(
#     data, sample_period, 1
# )

tot_noise = 0
tot_signal = 0
n_signal = 0
n_noise = 0

diff = 10
for i in range(len(freq_data[1])):
    if freq_data[1][i] > 5000 - diff and freq_data[1][i] < 5000 + diff:
        tot_signal += fft_data[1][i]
        n_signal += 1
    elif freq_data[1][i] > 0:
        tot_noise += fft_data[1][i]
        n_noise += 1

tot_noise /= n_noise
tot_signal /= n_signal

print("Noice total: " + str(tot_noise))
print("Signal total: " + str(tot_signal))

# SNR = 10 * np.log10(tot_signal / tot_noise)
SNR = tot_signal - tot_noise
print("SNR: " + str(SNR))

plot_data_single(
    freq_data[1],
    fft_data[1],
    "Frequency [Hz]",
    "PDS [dB]",
    min(freq_data[1]),
    max(freq_data[1]),
    -300,
    max(fft_data[1]) + 10,
)
plt.show()

plot_data_single(
    freq_data_hanning[1],
    fft_data_hanning[1],
    "Frequency [Hz]",
    "PDS [dB]",
    min(freq_data[1]),
    max(freq_data_hanning[1]),
    min(fft_data_hanning[1]) - 10,
    max(fft_data_hanning[1]) + 10,
)
plt.axhline(y=-159.034, color="r", linestyle="dashed", label="Maksimal støyeffekt")
plt.legend()
plt.show()
