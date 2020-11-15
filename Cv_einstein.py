## Calculation of Einstein oscillator contributions to heat capacity (Cv)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

########################## EINSTEIN OSCILLATORS ##########################
##
##WE_array = [wE_1, wE_2, wE_3]
##
##ein_array = []
##
##for i in WE_array:
##    ein_array.append(((i*CONV/ITEMP) \
##    **2.0*math.exp(i*CONV/ITEMP))/((math.exp(i*CONV/ITEMP)-1)**2.0))
##
##Cv_e = 3.*AVO*BOLTZ*(q_1*ein_array[0] + q_2*ein_array[1] + q_3*ein_array[2])
##
##print('Contribution from Einstein oscillators to Cv: ', format(Cv_e, '.2f'), ' J/mol.K')
##
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

##print(Cv_e)
