import numpy as np


muabo = np.genfromtxt("./muabo.txt", delimiter=",")
muabd = np.genfromtxt("./muabd.txt", delimiter=",")

red_wavelength = 600  # Replace with wavelength in nanometres
green_wavelength = 515  # Replace with wavelength in nanometres
blue_wavelength = 460  # Replace with wavelength in nanometres

wavelength = np.array([red_wavelength, green_wavelength, blue_wavelength])


def mua_blood_oxy(x):
    return np.interp(x, muabo[:, 0], muabo[:, 1])


def mua_blood_deoxy(x):
    return np.interp(x, muabd[:, 0], muabd[:, 1])


bvf = 0.01  # Blood volume fraction, average blood amount in tissue
oxy = 0.8  # Blood oxygenation

# Absorption coefficient ($\mu_a$ in lab text)
# Units: 1/m
mua_other = 25  # Background absorption due to collagen, et cetera
mua_blood = mua_blood_oxy(wavelength) * oxy + mua_blood_deoxy(  # Absorption due to
    wavelength
) * (
    1 - oxy
)  # pure blood
mua = mua_blood * bvf + mua_other

# reduced scattering coefficient ($\mu_s^\prime$ in lab text)
# the numerical constants are thanks to N. Bashkatov, E. A. Genina and
# V. V. Tuchin. Optical properties of skin, subcutaneous and muscle
# tissues: A review. In: J. Innov. Opt. Health Sci., 4(1):9-38, 2011.
# Units: 1/m
musr = 100 * (17.6 * (wavelength / 500) ** -4 + 18.78 * (wavelength / 500) ** -0.22)

# mua and musr are now available as shape (3,) arrays
# Red, green and blue correspond to indexes 0, 1 and 2, respectively

# TODO calculate penetration depth

penetration_depth = np.sqrt(1 / (3 * mua * (musr + mua)))
print(
    f"Red: {penetration_depth[0]}, Green: {penetration_depth[1]}, Blue: {penetration_depth[2]}"
)
print("")


# Transmittion percentage
finger_depth = 0.015  # Units: m
C = np.sqrt(3 * mua * (musr + mua))
transmition = np.exp(-C * finger_depth)
print(f"Transmition of red waves: {transmition[0]*100} %")
print(f"Transmation of green waves: {transmition[1]*100} %")
print(f"Transmition of blue waves: {transmition[2]*100} %")
print("")


# Contrast
blood_diameter = 300e-6
transmition_low = np.exp(-C * blood_diameter)

## Variable changes due to higher blood volume fraction
bvf = 1  # Blood volume fraction, average blood amount in tissue
mua_other = 25  # Background absorption due to collagen, et cetera
mua_blood = mua_blood_oxy(wavelength) * oxy + mua_blood_deoxy(  # Absorption due to
    wavelength
) * (
    1 - oxy
)  # pure blood
mua = mua_blood * bvf + mua_other
C = np.sqrt(3 * mua * (musr + mua))
transmition_high = np.exp(-C * blood_diameter)


contrast = abs(transmition_high - transmition_low) / transmition_low
print(f"Contrast of red waves: {contrast[0]}")
print(f"Contrast of green waves: {contrast[1]}")
print(f"Contrast of blue waves: {contrast[2]}")
print("")
