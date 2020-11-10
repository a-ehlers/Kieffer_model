## This program is hard-coded with zircon parameters

import math
from scipy.integrate import quad

## Input parameters

Vs = 3.97 # kilometers/second
Vp = 8.06 # kilometers/second
Vmax = 4.87 # kilometers/second
Vol = 130.5 # A
Z = 2.0 # molecules/unit cell
Natoms = 6.0 # atoms/formula unit
wc_L = 142.0
wc_U = 608.0
q_c = 0.22
wE_1 = 974.0
q_1 = 0.055
wE_2 = 1000.0
q_2 = 0.11
wE_3 = 885.0
q_3 = 0.055

ITEMP = 300.0 # Kelvin

## Constants
AVO = 6.023e23 # 1/mole
SPEED = 3e10 # meters/second
BOLTZ = 1.38e-23 # Joules/Kelvin
PLANCK = 6.626e-34 # Joules.second
R = 8.3145 # Joules/mole.Kelvin
CONV = SPEED*PLANCK/BOLTZ

######################## EINSTEIN OSCILLATORS ##########################

WE_array = [wE_1, wE_2, wE_3]

ein_array = []

for i in WE_array:
    ein_array.append(((i*CONV/ITEMP) \
    **2.0*math.exp(i*CONV/ITEMP))/((math.exp(i*CONV/ITEMP)-1)**2.0))

Cv_e = 3.*AVO*BOLTZ*(q_1*ein_array[0] + q_2*ein_array[1] + q_3*ein_array[2])

print('Contribution from Einstein oscillators to Cv: ', format(Cv_e, '.2f'), ' J/mol.K')

##Cv = Cv_a + Cv_o + Cv_e
##
##print('The isochoric heat capacity for zircon at ', ITEMP, ' K is:', format(Cv, '.2f'), ' J/mol.K')

########################################################################
