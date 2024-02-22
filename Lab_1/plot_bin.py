from raspi_import import raspi_import
import matplotlib.pyplot as plt
import numpy as np


def plot_file_subplot(filepath):
    sample_period, data = raspi_import(filepath)

    data_1 = data[:, 0]
    data_2 = data[:, 1]
    data_3 = data[:, 2]
    data_4 = data[:, 3]
    data_5 = data[:, 4]

    dt = 1 / sample_period
    t = np.arange(0, len(data_1) * dt, dt) / 10e8

    plt.figure(figsize=(10, 8))

    plt.subplot(5, 1, 1)
    plt.plot(t, data_1)
    plt.title("ADC 1")

    plt.subplot(5, 1, 2)
    plt.plot(t, data_2)
    plt.title("ADC 2")

    plt.subplot(5, 1, 3)
    plt.plot(t, data_3)
    plt.title("ADC 3")

    plt.subplot(5, 1, 4)
    plt.plot(t, data_4)
    plt.title("ADC 4")

    plt.subplot(5, 1, 5)
    plt.plot(t, data_5)
    plt.title("ADC 5")

    plt.tight_layout()
    plt.show()


def plot_file_together(filepath):
    sample_period, data = raspi_import(filepath)

    data_1 = data[:, 0]
    data_2 = data[:, 1]
    data_3 = data[:, 2]
    data_4 = data[:, 3]
    data_5 = data[:, 4]

    dt = 1 / sample_period
    t = np.arange(0, len(data_1) * dt, dt) / 10e8

    plt.plot(t, data_1, label="ADC 1")
    plt.plot(t, data_2, label="ADC 2")
    plt.plot(t, data_3, label="ADC 3")
    plt.plot(t, data_4, label="ADC 4")
    plt.plot(t, data_5, label="ADC 5")
    plt.legend()
    plt.show()


# filepath_relative = "/foo7.bin"

# plot_data_subplot(filepath_relative)
# plot_data_together(filepath_relative)
