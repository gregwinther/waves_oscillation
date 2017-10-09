''' 
Simple program that shows how Fourier transforms are done in Python.

Sebastian G. Winther-Larsen (2017)
'''

from matplotlib import pyplot as plt
import numpy as np

Fs = 1000.0                       # Sampling frequency
delta_t = 1.0/Fs                # Time b/w each sample
N = 1024                        # No of samples
t =  np.arange(N) * delta_t    # Time array

# Synthesizing signal: sum of 50 Hz sine and 120 Hz cosine
x = 0.7*np.sin(2*np.pi*50*t) + np.cos(2*np.pi*120*t)

# Adding random signal to signal above
x = x + 1.2*np.random.randn(len(t))

# FFT
X = np.fft.fft(x, N) / N

# Frequecy array for plotting
freq = (Fs/2) * np.linspace(0, 1, N/2)

# Plotting
plt.figure(1)
plt.subplot(211)
plt.title("FFT")
plt.plot(t, x)
plt.ylabel("Original signal, Hz")
plt.xlabel("t [s]")
plt.subplot(212)
plt.plot(freq, 2*np.real(X[0:round(N/2)])) # Half of Fourier spectrum
plt.ylabel("Fourier spectrum, amplitude")
plt.xlabel("Frequency [Hz]")
plt.show()