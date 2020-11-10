## This program is hard-coded with zircon parameters

import math
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

########################### OPTIC BOX ##################################

x_L = wc_L*CONV/ITEMP #define lower bound of optic box integral

x_U = wc_U*CONV/ITEMP #define upper bound of optic box integral

##result_optic,error_optic = quad(lambda x: ((x**2*math.exp(x))/((x_U-x_L)*(math.exp(x)-1)**2)), x_L, x_U)

def optic(x):
    return ((x**2.*math.exp(x))/((x_U-x_L)*(math.exp(x)-1.0)**2.))

optic_quad, error = quad(optic, x_L, x_U)
##print(optic_quad)

Cv_o = 3.*AVO*BOLTZ*(1.0-1./(Natoms*Z)-q_c)*optic_quad

##print('Contribution from optic box to Cv: ', format(Cv_o, '.2f'), ' J/mol.K')
########################################################################
