import matplotlib.pyplot as plt
import numpy as np
from fft_converter import *
from data_handling import *
import scipy.signal as sig

# file_path = "txt_files/transmittion/01.txt"
# file_path = "txt_files/reflection/01.txt"
file_path = "txt_files/robusthet/panne.txt"


x_data, y_data, z_data = [], [], []

# Open the file and read line by line
with open(file_path, "r") as file:
    for line in file:
        # Split the line into components, assuming they are separated by spaces
        parts = line.split()
        # Convert each part to float and append to respective lists
        if len(parts) == 3:  # Ensure there are exactly three columns
            x_data.append(float(parts[0]))
            y_data.append(float(parts[1]))
            z_data.append(float(parts[2]))

# Convert lists to a NumPy array
data_array = np.array([x_data, y_data, z_data]).T  # Transpose to get columns correctly

time = np.linspace(0, 30, len(x_data))
x_data = sig.detrend(x_data)
y_data = sig.detrend(y_data)
z_data = sig.detrend(z_data)


fs = 40  # Example sampling rate in Hz
Nyq = fs / 2
low = 0.5 / Nyq
high = 4 / Nyq  # Example high cut-off, adjust as needed
b, a = sig.butter(N=4, Wn=[low, high], btype="band")

x_data = sig.filtfilt(b, a, x_data)
y_data = sig.filtfilt(b, a, y_data)
z_data = sig.filtfilt(b, a, z_data)

x_data_hanning = single_hanning_window(x_data)
y_data_hanning = single_hanning_window(y_data)
z_data_hanning = single_hanning_window(z_data)


# plt.plot(time, x_data, label="R", color="red")
# plt.plot(time, y_data, label="G", color="green")
# plt.plot(time, z_data, label="B", color="blue")

plt.plot(time, x_data_hanning, label="R (Hanning)", color="orange")
plt.plot(time, y_data_hanning, label="G (Hanning)", color="lime")
plt.plot(time, z_data_hanning, label="B (Hanning)", color="cyan")
plt.legend()
plt.show()

fft_x_data, freq_x_data = single_fft_converter(x_data, 1 / 40)
fft_y_data, freq_y_data = single_fft_converter(y_data, 1 / 40)
fft_z_data, freq_z_data = single_fft_converter(z_data, 1 / 40)

fft_x_data_hanning, freq_x_data_hanning = single_fft_converter(x_data_hanning, 1 / 40)
fft_y_data_hanning, freq_y_data_hanning = single_fft_converter(y_data_hanning, 1 / 40)
fft_z_data_hanning, freq_z_data_hanning = single_fft_converter(z_data_hanning, 1 / 40)

# plt.plot(freq_x_data*60, fft_x_data, label="R", color="red")
# plt.plot(freq_y_data*60, fft_y_data, label="G", color="green")
# plt.plot(freq_z_data * 60, fft_z_data, label="B", color="blue")

plt.plot(
    freq_x_data_hanning * 60, fft_x_data_hanning, label="R (Hanning)", color="orange"
)
plt.plot(
    freq_y_data_hanning * 60, fft_y_data_hanning, label="G (Hanning)", color="lime"
)
plt.plot(
    freq_z_data_hanning * 60, fft_z_data_hanning, label="B (Hanning)", color="cyan"
)

plt.xlim(0, 200)
plt.ylim(-200, 10)
plt.legend()
plt.show()

find_pulse(freq_x_data_hanning, fft_x_data_hanning)
find_pulse(freq_y_data_hanning, fft_y_data_hanning)
find_pulse(freq_z_data_hanning, fft_z_data_hanning)
