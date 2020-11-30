## Calculation of Einstein oscillator contributions to Helmholtz free energy (F*)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

F_e = []

WE_array = [wE_1, wE_2, wE_3]

for i in ATEMP:
    ein_array = []

    for j in WE_array:
        ein_array.append(math.log(1.0 - math.exp(-j*CONV/i)))

    einstein_F = 3.*AVO*BOLTZ*i*(q_1*ein_array[0] + q_2*ein_array[1] + q_3*ein_array[2])

    F_e.append(einstein_F)
