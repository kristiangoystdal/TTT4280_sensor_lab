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


def plot_side_by_side(lags, cross, f_lags, f_cross, ylim, lim1, lim2, scale):

    # Create a figure and a set of subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    plt.rcParams.update({"font.size": 13})

    # First subplot
    ax1.plot(f_lags, f_cross, marker="o")
    ax1.set_xlim(-lim1, lim2)  # Set limits for x-axis
    ax1.set_ylim(ylim, None)
    ax1.set_aspect("equal", adjustable="box")  # Make the plot square
    ax1.set_title("Uten interpolering")
    ax1.grid(True)
    ax1.set_xlabel("Tidsforskyvning [l]", fontsize=14)
    ax1.set_ylabel("Krysskorrelasjon", fontsize=14)

    ax1.tick_params(axis="both", which="major", labelsize=12)  # Set tick size
    ax1_xticks = np.linspace(-lim1, lim2, num=5)  # Adjust 'num' for more or fewer ticks
    upper_ylim = ax1.get_ylim()[1]  # Dynamic upper limit based on the data
    ax1_yticks = np.arange(ylim, upper_ylim + 2.5, 2.5)
    ax1.set_xticks(ax1_xticks)
    ax1.set_yticks(ax1_yticks)

    # Second subplot
    ax2.plot(lags, cross, "r", marker="o")
    ax2.set_xlim(-lim1 * scale, lim2 * scale)  # Set limits for x-axis
    ax2.set_ylim(ylim * scale, None)
    ax2.set_aspect("equal", adjustable="box")  # Make the plot square
    ax2.set_title("Med interpolering")
    ax2.grid(True)
    ax2.set_xlabel("Tidsforskyvning [l]", fontsize=14)
    ax2.set_ylabel("Krysskorrelasjon", fontsize=14)

    ax2.tick_params(axis="both", which="major", labelsize=12)  # Set tick size
    ax2.set_xticks(ax1_xticks * scale)
    ax2.set_yticks(ax1_yticks * scale)

    # fig.suptitle(title)
    plt.tight_layout()
    plt.show()


def plot_single(x, y, title, xlabel, ylabel, xlim1, xlim2, ylim1, ylim2, marker, grid):
    plt.plot(x, y, marker=marker)
    plt.title(title)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xlim(xlim1, xlim2)
    plt.ylim(ylim1, ylim2)
    plt.tick_params(axis="both", which="major", labelsize=12)
    plt.grid(grid)
    plt.show()
