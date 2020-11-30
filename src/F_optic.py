## Calculation of optic mode contributions to Helmholtz free energy (F*)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

F_o = []

for i in ATEMP:
    x_L = wc_L*CONV/i #define lower bound of optic box integral
    
    x_U = wc_U*CONV/i #define upper bound of optic box integral
    
    def optic(x):
        return (math.log(1.0 - math.exp(-x)))

    optic_quad, error = quad(optic, x_L, x_U)
    
    optic_F = 3.*AVO*BOLTZ*i*(1.0/(x_U - x_L))*(1.0-1./(Natoms*Z)-q_c)*optic_quad

    F_o.append(optic_F)
