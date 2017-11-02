'''
Code segment for problem 20, chapter 5.
This is not a functioning program, parameters missing:
N, omega_b, delta_t, A, omega_t

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np

phase = np.zeros(N) # Empty array for phase values

# Phase computation

phase[1] = 0.0

for i in range(N-1):
    phase[i+1] = phase[i] + omega_b * delta_t*(1.0 + A*np.sin(omega_t*t[i]))

FM_signal = np.sin(phase)
