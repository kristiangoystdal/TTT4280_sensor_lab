import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Specify the path to your CSV file
csv_file_path = "garmin_data/csv_files/reflection.csv"

# Read the CSV file using pandas
df = pd.read_csv(csv_file_path)

# Extract the second column
heart_rate = df.iloc[:, 2]  # iloc[:, 1] selects the second column

# Generate a time series for the x-axis: each value is 1 second later than the previous one
time_series_seconds = np.arange(len(heart_rate))

# Convert the time series from seconds to 'minutes:seconds' format
time_series_min_sec = [
    f"{int(time // 60)}:{time % 60:02d}" for time in time_series_seconds
]

# Plot the second column, using the time series as the x-axis
plt.figure(figsize=(10, 6))
plt.plot(
    time_series_seconds, heart_rate
)  # Plot with seconds as x-axis for accuracy in plot

# Optionally, you can set the x-ticks to show the 'minutes:seconds' format
# This part might need adjustment based on the density of your data points to keep the x-axis readable
plt.xticks(
    time_series_seconds[::60], time_series_min_sec[::60], rotation=45
)  # Adjust stride as needed

plt.title("Plot of the Second Column over Time")
plt.xlabel("Time (minutes:seconds)")
plt.ylabel(heart_rate.name)
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()

avg = np.mean(heart_rate)
print("Gjennomsnittspuls fra smartklokke: %f" % avg)
