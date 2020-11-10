## This program is hard-coded with zircon parameters

import math
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

######################### ACOUSTIC MODES ###############################

u2 = (2./(Vs**(-3.) + Vmax**(-3.)))**(1./3.)
u1 = (1./(2.*(Vs**(-3.)) - u2**(-3.)))**(1./3.)
u3 = Vp

U_array = [u1, u2, u3] # Directionally-averaged acoustic modes
X_array = [] # Nondimensionalized branches

Vmol = Vol*0.6023/Z

##print('Molar volume of zircon is: ', Vmol, 'cm^3')

##Kmax = (6.*(math.pi)*(math.pi)*(10**24)/Vol)**1./3.

##print('Radius of Kmax of Brillouin zone (cm-1): ', '{:e}'.format(Kmax))

for i in U_array:
    X_array.append((132.32*i/(Vol**(1./3.)))*CONV/ITEMP)

##print(X_array)

acoustic=[]

for i in X_array:
    # integrate acoustic function
    result_acoustic,error_acoustic = quad(lambda x: ((math.asin(x/i)**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(i**2.-x**2)*((math.exp(x))-1.)**2.)
, 0., i)

    acoustic.append(result_acoustic)

Cv_a = (3.*AVO*BOLTZ*(acoustic[0]+acoustic[1]+acoustic[2])/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)

print('Contribution from acoustic modes to Cv: ', format(Cv_a, '.2f'), ' J/mol.K')
########################################################################
