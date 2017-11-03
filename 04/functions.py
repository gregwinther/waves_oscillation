'''
Returns the left hand side of ODE dv/dt.
Used in fourth order Runge-Kutta for numerical
solution of two coupled ODEs.

Supposed to model a forced harmonic oscillation where the
external force only works a given time.

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np

def forced_oscillation(y, v, t, params):

    if t < params["end"]:
        dvdt = - params["A"]*v - params["B"]*np.cos(params["D"]*t)
    else:
        dvdt = - params["A"]*v - params["B"]*y

    return dvdt
