'''
Example program that models forced oscillations
where the external force acts only for a certain time.

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np
from matplotlib import pyplot as plt

# Importing solver
from rungekutta4 import *

# Constants and parameters
omega = 100
Q = 25
m = 1.0e-2
k = m*omega*omega
b = m*omega/Q
F = 40
T = 6.0
params = {  "A"   : b/m,
            "B"   : omega*omega,
            "C"   : F/m,
            "D"   : omega,
            "end" : T/2.0,
            "func": forced_oscillation }

# Number of steps and step size
N = 2e4
delta_t = T/N

# Allocating arrays
y = np.zeros(int(N))
v = np.zeros(int(N))
t = np.zeros(int(N))

for i in range(int(N-1)):

    y[i+1], v[i+1], t[i+1] = rk4r(y[i], v[i], t[i], delta_t, params)


# Plotting
plt.plot(t, y)
plt.xlabel("Time (arbitrary unit)")
plt.ylabel("Oscillation (arbitrary unit)")
plt.xlim([-0.2, T])
plt.ylim([-np.max(y)*1.2, np.max(y)*1.2])
plt.show()
