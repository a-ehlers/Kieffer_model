## Calculation of Einstein oscillator contributions to heat capacity (Cv*)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

Cv_e = []

WE_array = [wE_1, wE_2, wE_3]

for i in ATEMP:
    ein_array = []

    for j in WE_array:
        ein_array.append(((j*CONV/i) \
        **2.0*math.exp(j*CONV/i))/((math.exp(j*CONV/i)-1)**2.0))

    einstein_Cv = 3.*AVO*BOLTZ*(q_1*ein_array[0] + q_2*ein_array[1] + q_3*ein_array[2])

    Cv_e.append(einstein_Cv)
