from plot_data import *
from raspi_import import raspi_import
import numpy as np
import scipy.signal as sig
from functions import *

sample_period, data = read_file()
num_of_ADC = 3

data = sig.detrend(data, axis=1)

if isinstance(sample_period, (int, float)):
    dt = sample_period
    x_axis = np.arange(0, len(data[0]) * dt, dt)
    x_axis = [x_axis] * num_of_ADC


# Interpolasjon
inter_x_axis = []
inter_data = []
for i in range(num_of_ADC):
    temp_x_axis, temp_data = interpolate(x_axis[i], data[i])
    inter_x_axis.append(temp_x_axis)
    inter_data.append(temp_data)


plot_data_subplot_len(inter_x_axis, inter_data, num_of_ADC, "Signal", 0, 1)
7
N = len(inter_data[0])
sample_frequency = 1 / sample_period

lags, lags_ms, cross = kryss_korrelasjon_list(sample_frequency * 2 - 1, inter_data)

plot_data_subplot_len(lags, cross, num_of_ADC, "Cross-correlation", -100, 100)

# for inter_data_row in inter_data:
#     inter_data_row= inter_data[0]
# lags1,lags_ms1,cross1 = kryss_korrelasjon_list(sample_frequency*2-1, inter_data)
# plot_data_subplot_len(lags, cross, num_of_ADC, "Cross-correlation", -100, 100)


num_samples_delay, num_ms_delay = find_delay_list(cross, N, sample_frequency)

print("")
print(f"Forsinkelse i prøver: {num_samples_delay}")
print(f"Forsinkelse i millisekunder: {num_ms_delay}")

rad_angle, degree_angle = angle_finder(num_ms_delay)

print("")
print(f"Vinkelen til signalet i radianer: {rad_angle}")
print(f"Vinkelen til signalet i grader: {degree_angle}")
