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

########################### OPTIC BOX ##################################

x_L = wc_L*CONV/ITEMP #define lower bound of optic box integral

x_U = wc_U*CONV/ITEMP #define upper bound of optic box integral

##result_optic,error_optic = quad(lambda x: ((x**2*math.exp(x))/((x_U-x_L)*(math.exp(x)-1)**2)), x_L, x_U)

def optic(x):
    return ((x**2*math.exp(x))/((x_U-x_L)*(math.exp(x)-1)**2))

optic_quad, error = quad(optic, x_L, x_U)
##print(optic_quad)

Cv_o = 3.*AVO*BOLTZ*(1.0-1./(Natoms*Z)-q_c)*optic_quad

print('Contribution from optic box to Cv: ', format(Cv_o, '.2f'), ' J/mol.K')
########################################################################
