'''
Another way to do wavelet transform?

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import soundfile as sf

data, Fs = sf.read("svarttrost2.wav")
widths = np.arange(1, 31)
cwtmatr = signal.cwt(data[:, 1], signal.morlet)
plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='magma', aspect='auto',
            vmax = abs(cwtmatr).max(), vmin = -abs(cwtmatr).max())
#plt.imshow(cwtmatr)

plt.show()
