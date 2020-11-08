## This program is hard-coded with zircon parameters

import math
from scipy.integrate import quad

## Input parameters

Vs = 3.97 # kilometers/second
Vp = 8.06 # kilometers/second
Vmax = 4.87 # kilometers/second
Vol = 130.5 # Angstroms^3
Z = 2 # molecules/unit cell
Natoms = 6 # atoms/formula unit
wc_L = 142
wc_U = 608
q_c = 0.22
wE_1 = 974
q_1 = 0.055
wE_2 = 1000
q_2 = 0.11
wE_3 = 885
q_3 = 0.055

ITEMP = 300 # Kelvin

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

Kmax = (6.*(math.pi)*(math.pi)*(10**24)/Vol)**1./3.

##print('Radius of Kmax of Brillouin zone (cm-1): ', '{:e}'.format(Kmax))

for i in U_array:
    X_array.append((132.32*i/(Vol**(1./3.)))*CONV/ITEMP)

acoustic_1 = X_array[0]
acoustic_2 = X_array[1]
acoustic_3 = X_array[2]

def integrand(x):
    return ((math.asin(x/acoustic_1)**2.)*x)/(math.sqrt(acoustic_1**2.-x**2.)*(math.exp(x)-1.))

SUM1 = quad(integrand, 0, acoustic_1)

def integrand(x):
    return ((math.asin(x/acoustic_2)**2.)*x)/(math.sqrt(acoustic_2**2.-x**2.)*(math.exp(x)-1.))

SUM2 = quad(integrand, 0, acoustic_2)

def integrand(x):
    return ((math.asin(x/acoustic_3)**2.)*x)/(math.sqrt(acoustic_3**2.-x**2.)*(math.exp(x)-1.))

SUM3 = quad(integrand, 0, acoustic_3)

print(SUM1[0], SUM2[0], SUM3[0])

SUM = SUM1[0] + SUM2[0] + SUM3[0]

E_a = (3.*AVO*BOLTZ*ITEMP*SUM/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)

print('Contribution from acoustic modes to E*: ', format(E_a, '.2f'), ' J')

##########################################################################

########################### OPTIC MODES ################################

x_L = wc_L*CONV/ITEMP

x_U = wc_U*CONV/ITEMP

##print(x_L, x_U)

def integrand(x):
    return x/((x_U - x_L)*(math.exp(x) - 1))

optic = quad(integrand, x_L, x_U)

##print(optic)

E_o = 3.*AVO*BOLTZ*ITEMP*(1-1./(Natoms*Z)-q_c)*optic[0]

print('Contibution from optic box to E*: ', format(E_o, '.2f'), ' J')

##########################################################################

########################### OPTIC MODES ################################


WE_array = [wE_1, wE_2, wE_3]

ein_array = []

for i in WE_array:
    ein_array.append((i*CONV/ITEMP)/(math.exp((i*CONV/ITEMP))-1))

E_e = 3.*AVO*BOLTZ*ITEMP*(q_1*ein_array[0] + q_2*ein_array[1] + q_3*ein_array[2])

print('Contribution from Einstein oscillators to E*: ', format(E_e, '.2f'), ' J')

E = E_a + E_o + E_e

print('The internal energy of zircon at ', ITEMP, ' K is:', format(E, '.2f'), ' J')
