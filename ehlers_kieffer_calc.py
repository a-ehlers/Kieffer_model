## This program is hard-coded with zircon parameters

import math

## Input parameters

Vs = 3.97
Vp = 8.06
Vmax = 4.87
Vol = 130.5
Z = 2
Natoms = 6

## Constants
ITEMP = 298
AVO = 6.023*10**23
SPEED = 3*10**10
BOLTZ = 1.38*10**-16
PLANCK = 6.625*10**-27
R = 1.986467
CONV = SPEED*PLANCK/BOLTZ

######################### ACOUSTIC MODES ###############################

u2 = (2/(Vs**(-3) + Vmax**(-3)))**(1/3)
u1 = (1/(2*(Vs**(-3)) - u2**(-3)))**(1/3)
u3 = Vp

U_array = [u1, u2, u3]
W_array = []


Vmol = Vol*0.6023/Z

print('Molar volume of zircon is: ', Vmol, 'cm^3')

Kmax = (6*(math.pi)*(math.pi)*(10**24)/Vol)**1/3

print('Radius of Kmax of Brillouin zone (cm-1): ', '{:e}'.format(Kmax))

for i in U_array:
    W_array.append(132.32*i/(Vol**(1/3)))

print('Directionally-averaged acoustic modes are: ', U_array)

print('Maximum frequencies of acoustic branches are: ', W_array)


##################### DEBYE TEMP CALCULATION ###########################

## Calculation of Debye temperature (DTEMP)

ZK = 1/(u1**3) + 1/(u2**3)
VSH = (2/ZK)**(1/3)
V1 = (2/VSH**3) + 1/(u3**3)
VRH = (3/V1)**(1/3)
VRH2 = VRH*10**5
A1 = PLANCK/BOLTZ
A2 = 3*Natoms*AVO
A3 = 4*Vmol*math.pi
A4 = (A2/A3)**(1/3)

DTEMP = A1*A4*VRH2

print('The Debye temperature for zircon is: ', DTEMP, 'K.')

## Debye approximation of Cv and S

CON1 = 233.7818186*R
CON2 = (ITEMP**3)/(DTEMP**3)
CON3 = 77.92727286*R
CV = CON1*CON2
S = CON2*CON3

print('Debye approx. for the heat capacity is: ', CV, ' J/K')
print('Debye approx. for the entropy is: ', S, ' J/K')

########################################################################
