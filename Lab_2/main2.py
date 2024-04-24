from pprint import pprint
from plot_data import *
from raspi_import import raspi_import
import numpy as np
import scipy.signal as sig
from functions import *

folders = os.listdir("./angles_bin")
print("Files to plot:")
for i in range(0, len(folders)):
    print(str(i + 1) + ": " + folders[i])

folder_number = input("Choose angles to plot: ")
print("")
folder_name = "./angles_bin/angle_" + folder_number

# ----------------------------------------------------------------
list_of_interpolated_data_x = []
list_of_interpolated_data_y = []
list_of_lags = []
list_of_cross_correlation = []
list_of_delays_samples = []
list_of_delays_ms = []
list_of_angles_rad = []
list_of_angles_degree = []

num_of_ADC = 3
bin_filenames = os.listdir(folder_name)

plot_file = " "
plot_all = False
while True:
    if plot_all == False:
        plot_file = int(input("Plot file nr (1-10) or plot all (0): "))
        if plot_file < 0 or plot_file > 10:
            print("Exiting program...")
            break
        else:
            if plot_file == 0:
                plot_file = 1
                plot_all = True
    else:
        plot_file += 1

    if plot_all == True and plot_file == len(bin_filenames) + 1:
        print("Finised plotting")
        break

    print(
        f"Processing file {plot_file} of {len(bin_filenames)}: {bin_filenames[plot_file - 1]}",
        end="\r",
    )
    sample_period, data = raspi_import(folder_name + "/" + bin_filenames[plot_file - 1])
    data = np.transpose(data)
    scaling_factor = 0.0008058608
    data *= scaling_factor
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

    first_x = x_axis
    first_data = data
    first_N = len(data[0])

    # x_axis = inter_x_axis
    # data = inter_data
    # inter_x_axis = []
    # inter_data = []
    # for i in range(num_of_ADC):
    #     temp_x_axis, temp_data = interpolate(x_axis[i], data[i])
    #     inter_x_axis.append(temp_x_axis)
    #     inter_data.append(temp_data)

    # x_axis = inter_x_axis
    # data = inter_data
    # inter_x_axis = []
    # inter_data = []
    # for i in range(num_of_ADC):
    #     temp_x_axis, temp_data = interpolate(x_axis[i], data[i])
    #     inter_x_axis.append(temp_x_axis)
    #     inter_data.append(temp_data)

    # x_axis = inter_x_axis
    # data = inter_data
    # inter_x_axis = []
    # inter_data = []
    # for i in range(num_of_ADC):
    #     temp_x_axis, temp_data = interpolate(x_axis[i], data[i])
    #     inter_x_axis.append(temp_x_axis)
    #     inter_data.append(temp_data)

    N = len(inter_data[0])
    sample_frequency = 1 / sample_period

    f_lags, f_lags_ms, f_cross = kryss_korrelasjon_list(
        sample_frequency * 2 - 1, first_data, first_N
    )
    f_num_samples_delay, f_num_ms_delay = find_delay_list(
        f_cross, first_N, sample_frequency
    )
    list_of_delays_samples.append(f_num_samples_delay)
    list_of_delays_ms.append(f_num_ms_delay)
    rad_angle, degree_angle = angle_finder(f_num_ms_delay)
    list_of_angles_degree.append(degree_angle)
    list_of_angles_rad.append(rad_angle)

    lags, lags_ms, cross = kryss_korrelasjon_list(
        sample_frequency * 2 - 1, inter_data, N
    )
    num_samples_delay, num_ms_delay = find_delay_list(cross, N, sample_frequency)
    list_of_delays_samples.append(num_samples_delay)
    list_of_delays_ms.append(num_ms_delay)

    rad_angle, degree_angle = angle_finder(num_ms_delay)
    list_of_angles_degree.append(degree_angle)
    list_of_angles_rad.append(rad_angle)
    if plot_all == False:
        print("Done processing files.                         \n\n")

        print("Delay in samples:")
        pprint(num_samples_delay)

        print("\nDelay in ms:")
        pprint(num_ms_delay)

        print("\nAngles in radians:")
        pprint(rad_angle)

        print("\nAngles in degrees:")
        pprint(degree_angle)

        # plot_data_subplot_len(
        #     inter_x_axis,
        #     inter_data,
        #     num_of_ADC,
        #     "TIme Signal",
        #     0,
        #     1,
        # )
        # plot_data_subplot_len(
        #     f_lags,
        #     f_cross,
        #     num_of_ADC,
        #     "Cross-correlation",
        #     -50,
        #     50,
        # )
        # plot_data_subplot_len(
        #     lags,
        #     cross,
        #     num_of_ADC,
        #     "Cross-correlation",
        #     -100,
        #     100,
        # )

        plot_side_by_side(
            lags[0],
            cross[0],
            f_lags[0],
            f_cross[0],
            7.5,
            15,
            -5,
            2,
        )

if plot_all == True:
    print("\nDelay in samples:")
    pprint(list_of_delays_samples)

    print("\nDelay in ms:")
    pprint(list_of_delays_ms)

    print("\nAngles in radians:")
    pprint(list_of_angles_rad)

    print("\nAngles in degrees:")
    pprint(list_of_angles_degree)

    std, var = std_var(list_of_angles_degree)
    print(f"\nStandard deviation: {std}")
    print(f"Variance: {var}")