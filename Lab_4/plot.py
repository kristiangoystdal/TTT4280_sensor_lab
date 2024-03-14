import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_data(x, y, label_prefix=None):
    for i in range(len(x)):
        label_string = label_prefix + " " + str(i + 1)
        plt.plot(x[i], y[i], label=label_string)
        plt.xlabel("Time")
        plt.ylabel("Voltage")

    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_single(x, y, label_string=None, x_label=None, y_label=None):
    plt.plot(x, y, label=label_string)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def plot_csv(filename):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(filename)

    # Check if the DataFrame has at least two columns
    if len(df.columns) < 2:
        print("The CSV file must have at least two columns.")
        return

    plt.figure(figsize=(10, 6))  # Create a figure with a specified size
    plt.plot(df.iloc[:, 0], df.iloc[:, 1], label="Data")
    plt.title(f"{df.columns[1]} vs. {df.columns[0]}")  # Title with column names
    plt.xlabel(df.columns[0])  # Label for x-axis
    plt.ylabel(df.columns[1])  # Label for y-axis
    plt.xscale("log")

    # Step 1: Find the maximum y value
    max_y = df.iloc[:, 1].max()

    # Step 2: Calculate the y value that is 3 dB lower
    threshold_y = max_y - 3

    # Step 3: Find the index of the max value
    max_index = df.iloc[:, 1].idxmax()

    # Find the closest points on either side of the max value that are nearest to -3 dB
    # First, on the left side
    left_side = df.iloc[:max_index, 1]
    left_index = (np.abs(left_side - threshold_y)).argmin()

    # Then, on the right side
    right_side = df.iloc[max_index:, 1]
    right_index = (np.abs(right_side - threshold_y)).argmin() + max_index

    # Step 4: Add dashed vertical lines at these x-values
    left_freq = df.iloc[left_index, 0]
    right_freq = df.iloc[right_index, 0]
    plt.axvline(
        x=left_freq,
        color="red",
        linestyle="--",
        linewidth=1,
        label=f"{left_freq:.2f} Hz",
    )
    plt.axvline(
        x=right_freq,
        color="green",
        linestyle="--",
        linewidth=1,
        label=f"{right_freq:.2f} Hz",
    )

    # Ensure labels are not duplicated in the legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.show()
