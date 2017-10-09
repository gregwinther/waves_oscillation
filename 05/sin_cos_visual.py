'''
Program that visualises mean of sine-cosine products
The lesson lies in varying the second frequency slightly,
first to something b/w 102.0 and 270,
second so that |freq1 - freq2| < 2.0

Sebastian G. Winther-Larsen (2017)
'''

from matplotlib import pyplot as plt
import numpy as np

N = 1000
T = 1.0
t = np.linspace(0, T*(N-1)/N, N)
freq1 = 100.0
freq2 = 102.0
omega1 = 2*np.pi*freq1
omega2 = 2*np.pi*freq2
f = np.cos(omega1*t)
g = np.cos(omega2*t)

# Printing 'integral', no normalisation (1/N)
print("Integral: ", sum(f*g))

# Plotting
plt.plot(t, f*g, '-b')
plt.title("Product of Sine and Cosine")
plt.xlabel("Time [s]")
plt.ylabel("Signal [arb. unit]")
plt.plot((0, T), (0,0), '-r') # 
plt.show()
