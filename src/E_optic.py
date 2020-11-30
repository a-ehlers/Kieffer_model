## This program is hard-coded with zircon parameters

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

E_o = []

for i in ATEMP:
    x_L = wc_L*CONV/i #define lower bound of optic box integral
    
    x_U = wc_U*CONV/i #define upper bound of optic box integral
    
    def optic_E(x):
        return x/((x_U - x_L)*(math.exp(x) - 1))

    optic_quad, error = quad(optic_E, x_L, x_U)
    
    optic_E = 3.*AVO*BOLTZ*i*(1.0-1./(Natoms*Z)-q_c)*optic_quad

    E_o.append(optic_E)

##print(E_o)
