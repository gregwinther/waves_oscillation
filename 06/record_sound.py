'''
This program is an example of how to record sound 
in Python using sounddevice

Sebastian G. Winther-Larsen (2017)
'''

import sounddevice as sd
import numpy as np
from matplotlib import pyplot as plt

T  = 3.0            # Duration of recording
Fs = 11025          # Sampling rate
N = Fs*T            # For plotting 
t = np.linspace(0, T*(N-1)/N, N) 

# Recording
my_recording = sd.rec(int(T*Fs), samplerate = Fs, channels = 1)
sd.wait()                   # Waits until recording is done
sd.play(my_recording, Fs)   # Plays back recording

# Removing mean sound level
s = np.mean(my_recording)
y = my_recording - s

# Plotting
plt.plot(t, y, linewidth = 1)
plt.title("Recording")
plt.xlabel("Time [s]")
plt.ylabel("Microphone signal")
plt.show()
