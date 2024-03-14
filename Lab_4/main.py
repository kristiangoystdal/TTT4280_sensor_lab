from plot import *
from raspi_import import raspi_import
from fft_converter import *
import os
import numpy as np
import scipy.signal as sig
import pandas as pd
import shutil
from utility import *


def bin_file(folder):
    bin_folder = "bin_files/" + folder

    for filename in os.listdir():
        # If the file is a .bin file
        if filename.endswith(".bin"):
            # Move the file to the destination directory
            shutil.move(filename, os.path.join(bin_folder, filename))

    bin_filenames = os.listdir(folder)
    print("Files to plot:")
    for i in range(0, len(bin_filenames)):
        print(str(i) + ": " + bin_filenames[i])

    filepath_number = int(input("Choose file to plot: "))

    filepath_relative = "./" + folder + "/" + bin_filenames[filepath_number]

    return filepath_relative


def find_data(filename):
    sample_period, data = raspi_import(filename)
    data = sig.detrend(data[5:], axis=0)
    data = np.transpose(data)
    # skalerings_faktor = 0.0008058608
    # data *= skalerings_faktor
    data = data[3:]
    data = hanning_window(data)

    time = []
    if isinstance(sample_period, (int, float)):
        dt = sample_period
        time = np.arange(0, len(data[0]) * dt, dt)
        time = [time] * len(data)

    return time, data, sample_period


def single_file(folder):
    filename = bin_file(folder)
    time, data, sample_period = find_data(filename)

    plot_data(time, data, "Data")

    complex_data = data[1] + 1j * data[0]
    fft_freq, fft_data = complex_fft_converter(complex_data, sample_period)
    plot_single(fft_freq, fft_data, None, "Frequency [Hz]", "Magnitude [dB]")

    doppler_shift = find_highest_x(fft_freq, fft_data)
    f_0 = 24.13 * 10**9
    c = 3 * 10**8
    v_r = doppler_shift / (2 * f_0 / c)
    print("Speed of object is: {:.2f} m/s".format(v_r))
    print("")
    print("")


def data_handler(folderpath):
    data_path = "./bin_files/" + folderpath
    time = []
    data = []
    sample_periods = []
    fft_freq = []
    fft_data = []
    speeds = []

    for filename in os.listdir(data_path):
        t, d, sample_period = find_data(data_path + "/" + filename)
        time.append(t)
        data.append(d)
        sample_periods.append(sample_period)

    for i in range(len(data)):
        complex_data = data[i][1] + 1j * data[i][0]

        freq, fft = complex_fft_converter(complex_data, sample_periods[i])
        fft_freq.append(freq)
        fft_data.append(fft)

        doppler_shift = find_highest_x(freq, fft)

        f_0 = 24.13 * 10**9
        c = 3 * 10**8
        v_r = doppler_shift / (2 * f_0 / c)
        speeds.append(v_r)

    print("Speeds for measurements of " + str(folderpath) + ":")
    for v_r in speeds:
        print("Speed is: {:.5f} m/s".format(v_r))
    print(f"Average speed is {np.mean(speeds):.5f} m/s")
    print(f"Standard deviation is {np.std(speeds):.5f} m/s")
    print("")


def video_speeds(folderpath):
    for filenames in os.listdir(folderpath):
        speed_video = find_speed(folderpath + "/" + filenames)
        print(f"Speed from video of {filenames} is: {speed_video:.5f} m/s")


# ----------------------------------------------------------------------------------------------#
# This code is running


# Plot filter
plot_csv("csv/filter.csv")

# Plot a single bin file and find its speed
single_file("bin_files/forward_1")
single_file("bin_files/forward_2")
single_file("bin_files/backward")

# Finds speed from bin files
data_handler("forward_1")
data_handler("forward_2")
data_handler("backward")

# Finds speed from video
video_speeds("txt_files")
