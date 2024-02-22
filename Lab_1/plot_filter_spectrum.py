import pandas as pd
import matplotlib.pyplot as plt


def plot_csv(file_name):
    # Read the CSV file
    data = pd.read_csv(file_name)

    # Extracting columns
    frequency = data["Frequency (Hz)"]
    magnitude = data["Channel 1 Magnitude (dB)"]

    # Plotting with a logarithmic x-axis
    plt.figure(figsize=(10, 6))
    plt.semilogx(frequency, magnitude, marker="o")
    plt.axhline(y=-3, color="r", linestyle="--")  # -3 dB line

    # Adding a specific point at (29.6191, -3) with high zorder
    plt.scatter(29.6191, -3, color="green", zorder=3)

    plt.title("Frequency vs. Magnitude Plot (Logarithmic Scale)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True, which="both", ls="-")
    plt.xlim(0, 10**4)
    plt.savefig("Spectrum-plot")
    plt.show()


# Plotting the data from the CSV file
plot_csv("spectrum.csv")
