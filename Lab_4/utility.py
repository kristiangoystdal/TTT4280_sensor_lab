import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd


def find_highest_x(x, y):
    max_index = np.argmax(y)
    return x[max_index]


def find_highest_SNR(x, y, range):
    zero_freq_index = np.argmax(y)

    max_freq = x[zero_freq_index]

    exclude_indices = np.where((x >= max_freq - range) & (x <= max_freq + range))

    x_filtered = np.delete(x, exclude_indices)
    y_filtered = np.delete(y, exclude_indices)

    highest_SNR_index = np.argmax(y_filtered)
    highest_SNR = y_filtered[highest_SNR_index]

    return highest_SNR


def find_speed(filename):
    df = pd.read_csv(filename, sep="\t", skiprows=1, names=["time", "x_position"])
    # Prepare the data for linear regression model
    # The independent variable (x) is time, and the dependent variable (y) is the x position.
    X = df[["time"]].values
    y = df["x_position"].values

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict y values for the existing X values (to plot the regression line)
    y_pred = model.predict(X)

    # Extract the slope (coefficient) of the line
    slope = model.coef_[0]

    return slope
