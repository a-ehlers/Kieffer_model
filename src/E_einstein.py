## Calculation of Einstein modes contributions to heat capacity (E*)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

E_e = []

WE_array = [wE_1, wE_2, wE_3]

for i in ATEMP:
    ein_array = []

    for j in WE_array:
        ein_array.append((j*CONV/i)/(math.exp((j*CONV/i))-1))

    einstein_E = 3.*AVO*BOLTZ*i*(q_1*ein_array[0] + q_2*ein_array[1] + q_3*ein_array[2])

    E_e.append(einstein_E)

##print(E_e)
