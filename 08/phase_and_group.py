'''
This program is meant to illustrate the difference phase- and
group velocity.

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

# Making spatial wave packet
def phase_group_wavepacket(z, x_max, x_lambda, x_sigma):

    x = np.linspace(0, x_max * (N - 1) / N, N)
    x_center = x_max / 8
    x_freq = 1/ x_lambda
    y = np.cos((x - x_center) * np.pi * x_freq)
    convol = np.exp(-((x - x_center) / x_sigma) * ((x - x_center) / x_sigma))
    z = y * convol
    return x, z

# Fourier Transform of
def phase_group_fft(z, N, x_max):

    z_fft = np.fft.fft(z) / N
    A = 2 * np.abs(z_fft)
    theta = np.arctan2(z_fft.real, z_fft.imag)
    x_sample_freq = N/ x_max
    x_freq = np.linspace(0, x_sample_freq * (N - 1) / N, N)
    k = 2 * np.pi * x_freq

    # In order to pick out i_min, i_max
    # plt.plot(A)
    # plt.show()

    return A, theta, k

def phase_group_omega(i_min, i_max, k, dispersion):

    # Creating dictionary int the range of i_min and i_max
    omega = dict.fromkeys(range(i_min, i_max))

    if (dispersion == -1):
        delta_t = 0.015
        omega_factor = 44
        for i in omega:
            omega[i] = omega_factor * np.sqrt(k[i])

    if (dispersion == 0):
        delta_t = 0.015
        omega_factor = 9.5
        for i in omega:
            omega[i] = omega_factor * k[i]

    if (dispersion == 1):
        delta_t = 0.0065
        omega_factor = 5.5
        for i in omega:
            omega[i] = omega_factor * (k[i]**1.5)

    return omega, delta_t

def phase_group_wave(x, t, N, A, phase, k, omega, i_min, i_max):

    z_recon = np.zeros(N)
    for i in range(i_min, i_max):
        arg = k[i] * x - omega[i]*t + phase[i]
        z_recon += A[i] * np.cos(arg)

    return z_recon

def init():
    return 0

def animate(frame, data, line):

    # Unpacking data
    # data = [x, delta_t, N, A, phase, k, omega, i_min, i_max, x_max]
    data[0] = x
    data[1] = delta_t
    data[2] = N
    data[3] = A
    data[4] = phase
    data[5] = k
    data[6] = omega
    data[7] = i_min
    data[8] = i_max
    data[9] = x_max

    # Computing wave at time t
    t = delta_t * frame
    z_recon = phase_group_wave(x, t, N, A, phase, k, omega, i_min, i_max)

    line.set_data(x, z_recon)
    return line,


if __name__ == '__main__':

    # Choosing dispersion, can be
    # -1: Normal dispersion
    #  0: No dispersion
    # +1: Anomalous dispersion
    dispersion = 1

    # Creating a spatial wave packet
    N = 4000
    x_max = 40
    x_lambda = 1
    x_sigma = 2
    x, z = phase_group_wavepacket(N, x_max, x_lambda, x_sigma)

    # Spatial frequency analysis
    A, phase, k = phase_group_fft(z, N, x_max)

    # Possibility to pick out areas with high amplitude from freqency plot
    i_min = 23
    i_max = 59

    # Finding omega from dispersion relation
    omega, delta_t = phase_group_omega(i_min, i_max, k, dispersion)

    # Figure to plot on
    fig = plt.figure()
    line, = plt.plot([])
    plt.xlim(0, x_max)
    plt.ylim(-1.04, 1.04)
    if dispersion == -1:
        plt.title("Normal dispersion")
    if dispersion == 0:
        plt.title("No dispersion")
    if dispersion == +1:
        plt.title("Anomalous dispersion")

    # Animation arguments
    data = [x, delta_t, N, A, phase, k, omega, i_min, i_max, x_max]
    ani_args = (data, line)

    # Animate!
    ani = animation.FuncAnimation(fig, animate, frames=1200, init_func=None,
                    interval=20, fargs=ani_args)

    # Show figure
    plt.show()
