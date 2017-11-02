'''
Returns the left hand side of ODE dv/dt.
Used in fourth order Runge-Kutta for numerical
solution of two coupled ODEs.

Supposed to model a forced harmonic oscillation where the
external force only works a given time.

Sebastian G. Winther-Larsen (2017)
'''

def forced_oscillation(y, v, t, param):

    if t < param["end"]:
        dvdt = - param["A"]*v - param["B"]*np.cos(param["D"]*t)
    else:
        dvdt = - param["A"]*v - param["B"]*y

    return dvdt
