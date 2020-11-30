## Calculation of optic mode contributions to heat capacity (Cv*)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

Cv_o = []

for i in ATEMP:
    x_L = wc_L*CONV/i #define lower bound of optic box integral
    
    x_U = wc_U*CONV/i #define upper bound of optic box integral
    
    def optic(x):
        return ((x**2.*math.exp(x))/((x_U-x_L)*(math.exp(x)-1.0)**2.))

    optic_quad, error = quad(optic, x_L, x_U)
    
    optic_Cv = 3.*AVO*BOLTZ*(1.0-1./(Natoms*Z)-q_c)*optic_quad

    Cv_o.append(optic_Cv)
