from numpy.fft import fft, fftfreq, fftshift
import numpy as np
import math


def data_fft_converter(data, sample_period):
    dt = sample_period
    N_fft = 2 ** (math.ceil(math.log(len(data[0]), 2))) * 4
    data_freq = []
    data_fft = []
    for data_row in data:
        temp_fft = fft(data_row, N_fft)
        temp_fft = 20 * np.log(abs(temp_fft) / np.max(abs(temp_fft)))
        freq = fftfreq(N_fft, dt)
        freq = fftshift(freq)
        temp_fft = fftshift(temp_fft)
        data_fft.append(temp_fft)
        data_freq.append(freq)
    return (data_freq, data_fft)


def zero_padding_data_fft_converter(data, sample_period, row):
    dt = sample_period
    N_fft = 2 ** (math.ceil(math.log(len(data[0]), 2)))
    data_freq = []
    data_fft = []
    for i in range(len(data)):
        data[i] = data[row]
        data_row = data[i]
        if i != 0:
            N_fft *= 2
        temp_fft = fft(data_row, N_fft)
        temp_fft = 20 * np.log(abs(temp_fft) / max(abs(temp_fft)))
        freq = fftfreq(N_fft, dt)
        freq = fftshift(freq)
        temp_fft = fftshift(temp_fft)
        data_fft.append(temp_fft)
        data_freq.append(freq)
    print("FFT done")
    return data_freq, data_fft


def hanning_window(data):
    tempData = []
    for data_row in data:
        window = np.hanning(len(data_row))
        data_row *= window
        tempData.append(data_row)

    return tempData


def complex_fft_converter(complex_data, sample_period):
    N_fft = 2 ** math.ceil(math.log(len(complex_data), 2))
    fft_result = fft(complex_data, N_fft)
    fft_db = 20 * np.log10(np.abs(fft_result) / np.max(np.abs(fft_result)))
    freq = fftfreq(N_fft, sample_period)
    fft_db_shifted = fftshift(fft_db)
    freq_shifted = fftshift(freq)

    return freq_shifted, fft_db_shifted
