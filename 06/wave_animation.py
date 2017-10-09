'''
This program shows an example of how to make an
animation of a wave in python. In order to save the
animation some extra encoding packages are needed. 
These depend on the operating system.

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

k = 3
omega = 8
N = 1000

# Set up figure
fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(-2.5, 2.5))
line, = ax.plot([], [], linewidth = 2)

# Initialisation function
def init():
    line.set_data([], [])
    return line,

# Animation function, called sequentially
def animate(i):
    t = 0.01*i
    x = np.linspace(0, 20, N)
    y = 2.0 * np.sin(k*x - omega*t)
    line.set_data(x, y)
    return line,

# Call animator. blit=True means only re-draw changed parts
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200,\
                                interval=20, blit=True)

# Save animation
anim.save("wave_animation.mp4", fps=30)

plt.show()