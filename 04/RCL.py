'''
FYS2130 - Ch 4
Simulation of RCL circuit
This program is based on Maple computations

Sebastian G. Winther-Larsen (2017)
'''

from matplotlib import pyplot as plt
import numpy as np

R = 10.0
L = 20.0
C = 2.0e-6
w = 157.0
V0 = 10.0
N = 4000
t = np.linspace(0, 20, N)

#print(C*C*R*R - 4*C*L)

q = np.zeros(N)
rq = np.zeros(N)
particular = np.zeros(N)

alpha1 = -0.5 * (C*R - np.sqrt(complex(C*C*R*R - 4*C*L))) / (C*L)
alpha2 = -0.5 * (C*R + np.sqrt(complex(C*C*R*R - 4*C*L))) / (C*L)

numerator1 = C*L * (-R * np.sqrt(complex(C*C*R*R - 4*C*L)) + 2*C-4*L) * V0
denominator1 = 2*C*C*R*C*w*w*L*L - 8*w*w*L**2*C + C*C*R**4 - \
        6*R*R*C*L + 8*L*L - np.sqrt(complex(C*C*R*R - 4*C*L))*R**3*C + \
        4*R*np.sqrt(complex(C*C*R*R - 4*C*L))*L
factor1 = numerator1 / denominator1

numerator2 = C*L * (-R*np.sqrt(complex(C*C*R*R-4*C*L)) + R*R*C - 4*L) * V0
denominator2 = (R*R*C -4*L) *  (R*np.sqrt(complex(C*C*R*R - 4*C*L)) + \
       R*R*C - 2*L + w*w*C*L*L)
factor2 = numerator2 / denominator2

numerator3 = C*V0
denominator3 = R*R*C*C*w*w + 1 - 2*C*w*w*C*L + w**4*C*C*L*L
factor3 = numerator3 / denominator3

particular = np.cos(w*t) - np.cos(w*t)*w*w*C*L + np.sin(w*t)*w*C*R
q = np.exp(alpha1*t) * factor1 + np.exp(alpha2*t)*factor2 + particular*factor3

rq = np.real(q)
plt.plot(t, rq, '-b')
plt.title("RCL circuit")
plt.xlabel("t [s]")
plt.ylabel("Q [C]")
plt.show()
