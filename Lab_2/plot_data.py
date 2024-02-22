from raspi_import import raspi_import
import matplotlib.pyplot as plt
import numpy as np


def plot_data_subplot(sample_period, data):
    dt = sample_period
    t = np.arange(0, len(data[0]) * dt, dt)

    plt.figure(figsize=(10, 8))

    plt.subplot(5, 1, 1)
    plt.plot(t, data[0], color="blue")
    plt.title("ADC 1")

    plt.subplot(5, 1, 2)
    plt.plot(t, data[1], color="red")
    plt.title("ADC 2")

    plt.subplot(5, 1, 3)
    plt.plot(t, data[2], color="orange")
    plt.title("ADC 3")

    plt.subplot(5, 1, 4)
    plt.plot(t, data[3], color="green")
    plt.title("ADC 4")

    plt.subplot(5, 1, 5)
    plt.plot(t, data[4], color="purple")
    plt.title("ADC 5")

    plt.tight_layout()
    plt.show()


def plot_data_subplot_len(x_axis, data, lenght, title, xmin=-16000, xmax=16000):
    num_plots = lenght
    colors = [
        "blue",
        "green",
        "red",
        "cyan",
        "magenta",
        "yellow",
        "black",
        "purple",
        "orange",
        "brown",
    ]

    figsize_width = 10
    figsize_height_per_plot = 2
    figsize_height = num_plots * figsize_height_per_plot

    plt.figure(figsize=(figsize_width, figsize_height))

    for i in range(num_plots):
        plt.subplot(num_plots, 1, i + 1)
        plt.plot(x_axis[i], data[i], color=colors[i % len(colors)])
        plt.title(f"{title} {i+1}")
        plt.xlim(xmin, xmax)

    plt.tight_layout()
    plt.show()


def plot_data_together(data, sample_period):
    dt = sample_period
    t = np.arange(0, len(data[0]) * dt, dt)

    plt.plot(t, data[0], label="Data 1")
    plt.plot(t, data[1], label="Data 2")
    plt.plot(t, data[2], label="Data 3")
    plt.plot(t, data[3], label="Data 4")
    plt.plot(t, data[4], label="Data 5")
    plt.legend()
    plt.show()


def plot_pure_data_subplot(axis, data):
    plt.figure(figsize=(10, 8))

    plt.subplot(5, 1, 1)
    plt.plot(axis[0], data[0])
    plt.title("ADC 1")

    plt.subplot(5, 1, 2)
    plt.plot(axis[1], data[1])
    plt.title("ADC 2")

    plt.subplot(5, 1, 3)
    plt.plot(axis[2], data[2])
    plt.title("ADC 3")

    plt.subplot(5, 1, 4)
    plt.plot(axis[3], data[3])
    plt.title("ADC 4")

    plt.subplot(5, 1, 5)
    plt.plot(axis[4], data[4])
    plt.title("ADC 5")

    plt.tight_layout()
    plt.show()


def plot_pure_data_together(axis, data):
    # plt.plot(axis[0], data[0], label="Data 1")
    plt.plot(axis[1], data[1], label="Data 2")
    # plt.plot(axis[2], data[2], label="Data 3")
    # plt.plot(axis[3], data[3], label="Data 4")
    # plt.plot(axis[4], data[4], label="Data 5")
    plt.legend()
    plt.ylabel("PSD [dB]")
    plt.xlabel("Frequency [Hz]")
    plt.show()


def plot_data_subplot_2x2(axis, data):
    plt.figure(figsize=(10, 8))

    # First subplot (top-left)
    plt.subplot(2, 2, 1)
    plt.plot(axis[0], data[0])
    plt.title("ADC 1")

    # Second subplot (top-right)
    plt.subplot(2, 2, 2)
    plt.plot(axis[1], data[1])
    plt.title("ADC 2")

    # Third subplot (bottom-left)
    plt.subplot(2, 2, 3)
    plt.plot(axis[2], data[2])
    plt.title("ADC 3")

    # Fourth subplot (bottom-right)
    plt.subplot(2, 2, 4)
    plt.plot(axis[3], data[3])
    plt.title("ADC 4")

    plt.tight_layout()
    plt.show()
