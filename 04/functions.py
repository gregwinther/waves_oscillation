'''
Returns the left hand side of ODE dv/dt.
Used in fourth order Runge-Kutta for numerical
solution of two coupled ODEs.

Supposed to model a forced harmonic oscillation where the
external force only works a given time.

Here one can add other functions as well and change the function that is
called in the params dictionary in main program.

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np

def forced_oscillation(y, v, t, params):

    if t < params["end"]:
        dvdt = - params["A"]*v - params["B"]*y + params["C"]*np.cos(params["D"]*t)
    else:
        dvdt = - params["A"]*v - params["B"]*y

    return dvdt
