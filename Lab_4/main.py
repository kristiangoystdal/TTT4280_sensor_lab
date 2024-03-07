from plot_bin import *
from plot_data import *
from raspi_import import raspi_import
from fft_converter import *
import os
import numpy as np
import scipy.signal as sig
import pandas as pd
import shutil

bin_folder = "bin_files"

for filename in os.listdir():
    # If the file is a .bin file
    if filename.endswith(".bin"):
        # Move the file to the destination directory
        shutil.move(filename, os.path.join(bin_folder, filename))


bin_filenames = os.listdir("./bin_files")
print("Files to plot:")
for i in range(0, len(bin_filenames)):
    print(str(i) + ": " + bin_filenames[i])

filepath_number = int(input("Choose file to plot: "))

filepath_relative = "./bin_files/" + bin_filenames[filepath_number]


sample_period, data = raspi_import(filepath_relative)
data = sig.detrend(data[5:], axis=0)
data = np.transpose(data)
