## Calculation of acoustic mode contributions to internal energy (E*)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

E_a = []

for i in ATEMP:
    X_array = [] # Nondimensionalized branches
    for j in U_array:
        X_array.append((132.32*j/(Vol**(1./3.)))*CONV/i)
        
    acoustic = []

    for z in X_array:
        def f_acoustic(x):
            return ((math.asin(x/z)**2.)*x)/(math.sqrt(z**2.-x**2.)*(math.exp(x)-1.))
    
        acoustic_quad, error = quad(f_acoustic, 0., z)
        acoustic.append(acoustic_quad)
    
    acoustic_E = (3.*AVO*BOLTZ*i*(acoustic[0]+acoustic[1]+acoustic[2])/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)
    E_a.append(acoustic_E)

##print(E_a)
