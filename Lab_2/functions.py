import numpy as np
from raspi_import import *
import os
import shutil


def move_bin_files_to_folder(destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for file_name in os.listdir("."):
        if file_name.endswith(".bin"):
            shutil.move(
                os.path.join(".", file_name),
                os.path.join(destination_dir, file_name),
            )


def read_file():
    bin_files_dir = "./bin_files"  # Destination directory for .bin files
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


def kryss_korrelasjon(fs, x, y):
    N = len(x)
    lags = np.arange(-N + 1, N)
    lags_ms = lags / fs * 1000
    cross = np.correlate(x, y, mode="full")

    return lags, lags_ms, np.abs(cross)


def kryss_korrelasjon_list(fs, data):
    lags = []
    lags_ms = []
    cross = []
    for i in range(3):
        if i == 0:
            x = data[1]
            y = data[0]
        elif i == 1:
            x = data[2]
            y = data[0]
        else:
            x = data[2]
            y = data[1]
        N = len(x)
        lags.append(np.arange(-N + 1, N))
        lags_ms.append(lags / fs * 1000)
        cross.append(np.abs(np.correlate(x, y, mode="full")))

    return lags, lags_ms, cross


def find_delay(cross, N, fs):
    max_index = np.argmax(np.abs(cross))
    num_samples_delay = max_index - (N - 1)
    delay_milliseconds = num_samples_delay / fs * 1000

    return num_samples_delay, delay_milliseconds


def find_delay_list(cross, N, fs):
    delay_ms = []
    delay_sample = []
    for cross_row in cross:
        max_index = np.argmax(np.abs(cross_row))
        num_samples_delay = max_index - (N - 1)
        delay_sample.append(num_samples_delay)
        delay_milliseconds = num_samples_delay / fs * 1000
        delay_ms.append(delay_milliseconds)

    return delay_sample, delay_ms


def angle_finder(lags_ms):
    arc = np.arctan(
        np.sqrt(3)
        * (lags_ms[0] + lags_ms[1])
        / (lags_ms[0] - lags_ms[1] - 2 * lags_ms[2])
    )
    if lags_ms[2] > 0:
        arc += np.pi
    if -np.pi / 2 < arc < 0:
        arc += 2 * np.pi
    degree = arc * 180 / np.pi

    return arc, degree


def std_var(data):
    return np.std(data), np.var(data)


def interpolate(x_axis, data):
    new_x_axis = []
    for i in range(len(x_axis)):
        new_x_axis.append(x_axis[i])
        if i < len(x_axis) - 1:
            average = (x_axis[i] + x_axis[i + 1]) / 2
            new_x_axis.append(average)

    return new_x_axis, np.interp(new_x_axis, x_axis, data)
