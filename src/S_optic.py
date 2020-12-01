## Calculation of optic mode contributions to entropy (S)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

S_o = []

for i in ATEMP:
    x_L = wc_L*CONV/i #define lower bound of optic box integral
    
    x_U = wc_U*CONV/i #define upper bound of optic box integral
    
    def optic_1(x1):
        return x1/(math.exp(x1)-1.)

    optic_quad_1, error = quad(optic_1, x_L, x_U)

    optic_S_1 = 3.*AVO*BOLTZ*(1.0-1./(Natoms*Z)-q_c)*optic_quad_1

    # Set up second function

    def optic_2(x2):
        return math.log(1. - math.exp(-x2))

    optic_quad_2, error = quad(optic_2, x_L, x_U)
    
    optic_S_2 = 3.*AVO*BOLTZ*(1.0-1./(Natoms*Z)-q_c)*optic_quad_2

    S_o.append(optic_S_1 - optic_S_2)
