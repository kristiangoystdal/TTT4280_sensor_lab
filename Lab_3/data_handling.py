import numpy as np


def find_pulse(x_axis, data):
    max_index = np.argmax(data)
    max_freq = abs(x_axis[max_index])
    max_db_value = data[max_index]

    # Printing the results
    print(
        f": The frequency with the highest dB value is {max_freq} Hz with a magnitude of {max_db_value} dB."
    )
    print(f"Pulse is {max_freq*60} BPM")
