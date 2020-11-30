## Calculation of acoustic mode contributions to entropy (S*)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

S_a = []

S_a1 = []

S_a2 = []

for i in ATEMP:
    X_array = [] # Nondimensionalized branches
    for j in U_array:
        X_array.append((132.32*j/(Vol**(1./3.)))*CONV/i)
        
    acoustic_a = []

    acoustic_b = []

    for z in X_array:

        # function acoustic_A: first acoustic function
        def acoustic_A(x1):
            return ((math.asin(x1/z)**2.)*(x1))/(math.sqrt(z**2.-x1**2.)*((math.exp(x1))-1.))
    
        acoustic_quad_a, error = quad(acoustic_A, 0., z)
        acoustic_a.append(acoustic_quad_a)

        # function acoustic_B: second acoustic function
        def acoustic_B(x2):
            return ((math.asin(x2/z)**2.)*(math.log(1.0 - math.exp(-x2))))/(math.sqrt(z**2.-x2**2.))
    
        acoustic_quad_b, error = quad(acoustic_B, 0., z)
        acoustic_b.append(acoustic_quad_b)
    
    acoustic_S_a = (3.*AVO*BOLTZ*(acoustic_a[0]+acoustic_a[1]+acoustic_a[2])/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)
    S_a1.append(acoustic_S_a)

    acoustic_S_b = (3.*AVO*BOLTZ*(acoustic_b[0]+acoustic_b[1]+acoustic_b[2])/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)
    S_a2.append(acoustic_S_b)

for i in range(len(ATEMP)):
    S_a.append(S_a1[i] - S_a2[i])

##print(S_a)
