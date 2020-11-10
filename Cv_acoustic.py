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
