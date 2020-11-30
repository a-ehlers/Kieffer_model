## Calculation Cv and S using the Debye model

import math
import numpy as np

#import params.py for all input parameters
from params import *

##########################################################################

Cv_debye = []

S_debye = []

DTEMP = (PLANCK/BOLTZ)*((3*Natoms*AVO)/(4*math.pi*Vmol))**(1./3.)* \
        (3./(1./(U_array[0]**3.) + 1./(U_array[1]**3.) + 1./(U_array[2]**3.)))**(1./3.)*1.0e5

for i in ATEMP:

    Cv = 233.7818186*R*(i/DTEMP)*(i/DTEMP)*(i/DTEMP)
    S = 77.92727286*R*(i/DTEMP)*(i/DTEMP)*(i/DTEMP)

    Cv_debye.append(Cv)
    S_debye.append(S)

##print(Cv_debye)
##print(S_debye)
