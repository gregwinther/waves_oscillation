'''
Simple illustration of radiation from a dipole antenna

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np
from matplotlib import pyplot as plt

N = 1024
theta = np.linspace(-np.pi/2, 3*np.pi/2, N)
cos_theta = np.cos(theta)
intensity = np.log10(cos_theta * cos_theta * 1000)

# Removes negative frequencies
intensity[intensity < 0] = 0

plt.polar(theta, intensity)
plt.show()
