import numpy as np
import time
import matplotlib.pyplot as plt


def get_sin_wave_amplitude(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1) / 2


def get_triangle_wave_amplitude(freq, time):
    return (np.arcsin(np.sin(2 * np.pi * freq * time)) * 2 / np.pi + 1) / 2


def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)


if __name__=="__main__":
    t = np.linspace(-500, 500, 1000)
    w = get_triangle_wave_amplitude(10, t)
    plt.plot(t, w)
    plt.show()