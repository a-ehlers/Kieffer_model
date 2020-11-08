## This program is hard-coded with zircon parameters

import math

## Input parameters

Vs = 3.97 # km/s
Vp = 8.06 # km/s
Vmax = 4.87 # km/s
Vol = 130.5 # A
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

ITEMP = 300 # K

## Constants
AVO = 6.023e23 # 1/mol
SPEED = 3e10 # m/s
BOLTZ = 1.38e-23 # J/K
PLANCK = 6.626e-34 # J.s
R = 8.3145 # J/mol.K
CONV = SPEED*PLANCK/BOLTZ

##################### DEBYE TEMP CALCULATION ###########################

u2 = (2./(Vs**(-3) + Vmax**(-3)))**(1./3.)
u1 = (1./(2.*(Vs**(-3)) - u2**(-3)))**(1./3.)
u3 = Vp

Vmol = Vol*0.6023/Z

## Calculation of Debye temperature (DTEMP)

ZK = 1./(u1**3) + 1./(u2**3.)
VSH = (2/ZK)**(0.3333333)
V1 = (2./VSH**3) + 1./(u3**3.)
VRH = (3./V1)**(0.3333333)
VRH2 = VRH*1e5
A1 = PLANCK/BOLTZ
A2 = 3.0*Natoms*AVO
A3 = 4.0*Vmol*math.pi
A4 = (A2/A3)**(0.3333333)

DTEMP = A1*A4*VRH2

print('The Debye temperature for zircon is: ', format(DTEMP, '.2f'), 'K.')

## Debye approximation of Cv and S. Cv may be incorrect

CON1 = 233.7818186*R
CON2 = (ITEMP**3)/(DTEMP**3)
CON3 = 77.92727286*R
CV_debye = CON1*CON2
S_debye = CON2*CON3

print('Debye approx. for the heat capacity is: ', format(CV_debye, '.2f'), ' J/mol.K')
print('Debye approx. for the entropy is: ', format(S_debye, '.2f'), ' J/K')

########################################################################
