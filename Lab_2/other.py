from functions import *

vinkel_1 = [58.43, 56.9, 58.43, 58.43, 58.43, 58.47, 56.9, 56.9, 58.43, 58.43]
vinkel_2 = [176.8, 178.37, 178.37, 176.8, 178.37, 175.13, 178.37, 176.8, 178.37, 176.7]
vinkel_3 = [
    243.2,
    244.72,
    241.57,
    241.57,
    241.57,
    241.57,
    241.57,
    241.57,
    241.57,
    241.57,
]


std_1, var_1 = std_var(vinkel_1)
std_2, var_2 = std_var(vinkel_2)
std_3, var_3 = std_var(vinkel_3)

print(f"Standard deviation 1: {std_1}")
print(f"Standard deviation 2: {std_2}")
print(f"Standard deviation 3: {std_3}")

print(f"Variance 1: {var_1}")
print(f"Variance 2: {var_2}")
print(f"Variance 3: {var_3}")
