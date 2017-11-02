'''
Example program that models forced oscillations
where the external force acts only for a certain time.

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np
from matplotlib import pyplot as plt
from forced_oscillation import forced_oscillation

# Constants and parameters
omega = 100
Q = 25
m = 1.0e-2
k = m*omega*omega
b = m*omega/Q
F = 40
T = 6.0
parameters = {  "A"   : b/m,
                "B"   : omega*omega,
                "C"   : F/m,
                "D"   : omega,
                "end" : T/2.0,
                "func": "forced_oscillation.py" }

# Number of steps and step size
N = 2e4
delta_t = T/N

# Allocating arrays
y = np.zeros(N)
v = np.zeros(N)
t = np.zeros(N)

for i in range(N-1):

    # INCOMPLETE!
    y[i+1], v[i+1], t[i+1] = rk4(y[i], v[j], t[j], delta_t, parameters)

# Plotting
plt.plot(t, y)
plt.xlabel("Time (arbitrary unit)")
plt.ylabel("Oscillation (arbitrary unit)")
plt.set_xlim([-0.2, T])
plt.set_ylim([-np.max(A)*1.2, np.max(A)*1.2])
plt.show()
