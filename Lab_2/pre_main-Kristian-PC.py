import numpy as np
import matplotlib.pyplot as plt
from raspi_import import *
from functions import *

# Parametre for signalet
frequency = 1  # 1 Hz
sample_rate = 31250  # 31250 samples per second
duration = 1  # 1 second duration

# Generer tidsverdier
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
delay = 0.1
# Generer sinussignalene
sine1 = np.sin(2 * np.pi * frequency * t)
sine2 = np.sin(2 * np.pi * frequency * (t + delay))

# Beregn krysskorrelasjon
lags, lags_ms, cross = kryss_korrelasjon(sample_rate, sine1, sine2)

N = len(sine1)

num_samples_delay, num_ms_delay = find_delay(cross, N, sample_rate)


# Vis resultatene
print(f"Forsinkelse i prøver: {num_samples_delay}")
print(f"Forsinkelse i millisekunder: {num_ms_delay}")

# Plot signalene
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, sine1, label="Sine 1")
plt.plot(t, sine2, label="Sine 2")
plt.title("Sinussignaler")
plt.legend()

# Plot krysskorrelasjon
plt.subplot(2, 1, 2)
plt.plot(lags_ms, np.abs(cross))
plt.title("Krysskorrelasjon")
plt.xlabel("Forsinkelse (ms)")
plt.show()
