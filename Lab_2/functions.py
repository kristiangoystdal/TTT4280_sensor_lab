import numpy as np
from raspi_import import *
import os
import shutil

SQRT_3 = np.sqrt(3)
PI = np.pi
DEGREE_FACTOR = 180 / PI


def move_bin_files_to_folder(destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for file_name in os.listdir("."):
        if file_name.endswith(".bin"):
            shutil.move(
                os.path.join(".", file_name),
                os.path.join(destination_dir, file_name),
            )


def read_file(folder_name):
    bin_files_dir = folder_name  # Destination directory for .bin files
    move_bin_files_to_folder(bin_files_dir)

    bin_filenames = os.listdir(bin_files_dir)
    print("Files to plot:")
    for i in range(0, len(bin_filenames)):
        print(str(i) + ": " + bin_filenames[i])

    filepath_number = int(input("Choose file to plot: "))
    filepath_relative = os.path.join(bin_files_dir, bin_filenames[filepath_number])

    sample_period, data = raspi_import(
        filepath_relative
    )  # Assuming this function is defined elsewhere
    data = np.transpose(data)

    scaling_factor = 0.0008058608
    data *= scaling_factor

    return sample_period, data


def kryss_korrelasjon_list(fs, data, length):
    pairs = [(1, 0), (2, 0), (2, 1)]
    lags, lags_ms, cross = [], [], []
    for i, j in pairs:
        x, y = data[i], data[j]
        N = len(x)
        lags.append(np.arange(-length + 1, length))
        lags_ms.append(lags / fs * 1000)
        cross.append(np.abs(np.correlate(x, y, mode="full")))

    return lags, lags_ms, cross


def find_delay_list(cross, N, fs):
    delay_sample, delay_ms = [], []
    for cross_row in cross:
        max_index = np.argmax(np.abs(cross_row))
        num_samples_delay = max_index - (N - 1)
        delay_sample.append(num_samples_delay)
        delay_ms.append(num_samples_delay / fs * 1000)

    return delay_sample, delay_ms


def angle_finder(lags_ms):
    rad = -np.arctan(
        SQRT_3 * (lags_ms[0] + lags_ms[1]) / (lags_ms[0] - lags_ms[1] - 2 * lags_ms[2])
    )
    if lags_ms[2] > 0:
        rad = PI - rad
    else:
        if rad < 0:
            rad *= -1
        else:
            rad = 2 * PI - rad
    degree = rad * DEGREE_FACTOR

    return rad, degree


def std_var(data):
    return np.std(data), np.var(data)


def interpolate(x_axis, data):
    new_x_axis = [
        average
        for i in range(len(x_axis) - 1)
        for average in [x_axis[i], (x_axis[i] + x_axis[i + 1]) / 2]
    ]
    new_x_axis.append(x_axis[-1])

    return new_x_axis, np.interp(new_x_axis, x_axis, data)
