from functions import *
import matplotlib.pyplot as plt

vinkel_1 = [
    243.19793959904965,
    244.7150039539482,
    241.5748287131948,
    241.5748287131948,
    241.5748287131948,
    241.5748287131948,
    241.5748287131948,
    241.5748287131948,
    241.5748287131948,
    241.5748287131948,
]
vinkel_2 = [
    58.42517128680522,
    56.90179819083681,
    58.42517128680522,
    58.42517128680522,
    58.42517128680522,
    58.47360426754634,
    56.90179819083681,
    56.90179819083681,
    58.42517128680522,
    58.42517128680522,
]
vinkel_3 = [
    176.80206040095035,
    178.37356485189127,
    178.37356485189127,
    176.80206040095035,
    178.37356485189127,
    175.13113718925254,
    178.37356485189127,
    176.80206040095035,
    178.37356485189127,
    176.69569481984405,
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

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(vinkel_1))
plt.scatter(x, vinkel_1)
plt.show()

plt.scatter(x, vinkel_2)
plt.show()

plt.scatter(x, vinkel_3)
plt.show()
