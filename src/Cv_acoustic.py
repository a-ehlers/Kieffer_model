## Calculation of acoustic mode contributions to heat capacity (Cv*)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

Cv_a = []

for i in ATEMP:
    X_array = [] # Nondimensionalized branches
    for j in U_array:
        X_array.append((132.32*j/(Vol**(1./3.)))*CONV/i)
        
    acoustic = []

    for z in X_array:
        def acoustic_function_Cv(x):
            return ((math.asin(x/z)**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(z**2.-x**2.)*((math.exp(x))-1.)**2.)
    
        acoustic_quad_Cv, error = quad(acoustic_function_Cv, 0., z)
        acoustic.append(acoustic_quad_Cv)

    acoustic_Cv = (3.*AVO*BOLTZ*(acoustic[0]+acoustic[1]+acoustic[2])/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)
    Cv_a.append(acoustic_Cv)

