'''
Example of how to import wave files.
This is done with pysoundfile, which may be installed, as
it is not a standard package: 'pip install pysoundfile'
The sound can be played using sounddevice, install with
'pip install sounddevice'
When the file is imported FFT is applied.

Sebastian G. Winther-Larsen(2017)
'''

import sounddevice as sd
import soundfile as sf
import numpy as np
from matplotlib import pyplot as plt 


# Importing sound file data and samplerate
N = 2**16
data, samplerate = sf.read("piccoloHigh.wav", stop = N)

# Playing sound
sd.play(data, samplerate)

# The sound file is sample as a stereo signal
# Extracting only mono signal
mono_signal = data[:,0]

# FFT
fft_spectrum = (1.0/N) * np.fft.fft(mono_signal)

# Frequency array for plotting
freq = (samplerate/2) * np.linspace(0, 1, int(N/2))

# plotting
plt.figure()
plt.subplot(211)
plt.title("FFT of Piccolo Flute")
plt.plot(mono_signal, linewidth = 1) 
plt.subplot(212)
plt.plot(freq, np.real(fft_spectrum[0:int(len(fft_spectrum)/2)]), \
        linewidth = 1)
plt.show()