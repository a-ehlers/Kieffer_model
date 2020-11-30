## Calculation of Einstein oscillator contributions to entropy (S)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

##########################################################################

S_e = []

S_e1 = []

S_e2 = []

WE_array = [wE_1, wE_2, wE_3]

for i in ATEMP:
    ein_array_1 = []
    
    for j in WE_array:
        ein_array_1.append((j*CONV/i)/(math.exp(j*CONV/i)-1.0))

    einstein_S_1 = 3.*AVO*BOLTZ*(q_1*ein_array_1[0] + q_2*ein_array_1[1] + q_3*ein_array_1[2])

    S_e1.append(einstein_S_1)

    ein_array_2 = []
    
    for j in WE_array:
        ein_array_2.append(math.log(1.0 - math.exp(-(j*CONV/i))))

    einstein_S_2 = 3.*AVO*BOLTZ*(q_1*ein_array_2[0] + q_2*ein_array_2[1] + q_3*ein_array_2[2])

    S_e2.append(einstein_S_2)

for i in range(len(ATEMP)):
    S_e.append(S_e1[i] - S_e2[i])

##print(S_e)
