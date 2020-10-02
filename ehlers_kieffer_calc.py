## This program is hard-coded with zircon parameters

import math

## Input parameters

Vs = 3.97
Vp = 8.06
Vmax = 4.87
Vol = 130.5
Z = 2
Natoms = 6
wc_L = 142
wc_U = 608
q_c = 0.22
wE_1 = 974
q_1 = 0.055
wE_2 = 1000
q_2 = 0.11
wE_3 = 885
q_3 = 0.055

## Constants
ITEMP = 300 # K
AVO = 6.023*10**23 # 1/mol
SPEED = 3*10**10 # m/s
BOLTZ = 1.38*10**-23 # J/K
PLANCK = 6.626*10**-34 # J.s
R = 8.3145 # J/mol.K
CONV = SPEED*PLANCK/BOLTZ

######################### ACOUSTIC MODES ###############################

u2 = (2/(Vs**(-3) + Vmax**(-3)))**(1/3)
u1 = (1/(2*(Vs**(-3)) - u2**(-3)))**(1/3)
u3 = Vp

U_array = [u1, u2, u3] # Directionally-averaged acoustic modes
W_array = [] # Maximum frequencies of acoustic branches
X_array = [] # Nondimensionalized branches

Vmol = Vol*0.6023/Z

##print('Molar volume of zircon is: ', Vmol, 'cm^3')

Kmax = (6*(math.pi)*(math.pi)*(10**24)/Vol)**1/3

##print('Radius of Kmax of Brillouin zone (cm-1): ', '{:e}'.format(Kmax))

for i in U_array:
    W_array.append(132.32*i/(Vol**(1/3)))

for i in W_array:
    X_array.append(i*CONV/ITEMP)

acoustic_1 = round(X_array[0],1)
acoustic_2 = round(X_array[1],1)
acoustic_3 = round(X_array[2],1)

infile = open('disp_sine_table.txt') # Table 1 in Kieffer, 1979c
array = []

for line in infile:
    array.append([float(x) for x in line.split()])

array_new = []

for i in array:
    array_new = i
    if array_new[0] == acoustic_1:
        SUM1 = array_new[1]
        print(SUM1)
    if array_new[0] == acoustic_2:
        SUM2 = array_new[1]
        print(SUM2)
    if array_new[0] == acoustic_3:
        SUM3 = array_new[1]
        print(SUM3)

SUM = SUM1 + SUM2 + SUM3

Cv_a = (3*AVO*BOLTZ*SUM/(Natoms*Z))*(2/math.pi)*(2/math.pi)*(2/math.pi)

print('Contribution from acoustic modes to Cv: ', format(Cv_a, '.2f'), ' J/mol.K')
########################################################################

########################### OPTIC BOX ##################################

# f is Gaussian quadrature function: x^2*exp(x)/(xU-xL)*(exp(x)-1)^2

x_L = wc_L*CONV/ITEMP

x_U = wc_U*CONV/ITEMP

f = lambda X: ((x_U-x_L)/2)*(((((x_U-x_L)*X+x_U+x_L)/2)**2*math.exp(((x_U-x_L)* \
             X+x_U+x_L)/2))/((x_U - x_L)*(math.exp(((x_U-x_L)*X+x_U+x_L)/2)-1)**2))

##quad_2 = f(-math.sqrt(1/3)) + f(math.sqrt(1/3))

quad_3 = (5/9)*f(-math.sqrt(3/5)) + (8/9)*f(0) + (5/9)*f(math.sqrt(3/5))

##print(quad_3)

Cv_o = 3*AVO*BOLTZ*(1-1/(Natoms*Z)-q_c)*quad_3

print('Contibution from optic box to Cv: ', format(Cv_o, '.2f'), ' J/mol.K')
########################################################################

######################## EINSTEIN OSCILLATORS ##########################

WE_array = [wE_1, wE_2, wE_3]

x_WE_array = []

ein_array = []

for i in WE_array:
    x_WE_array.append(i*CONV/ITEMP)
    
for i in x_WE_array:
    ein_array.append((i**2*math.exp(i))/((math.exp(i)-1)**2))

Cv_e = 3*AVO*BOLTZ*(q_1*ein_array[0] + q_2*ein_array[1] + q_3*ein_array[2])

print('Contribution from Einstein oscillators to Cv: ', format(Cv_e, '.2f'), ' J/mol.K')

Cv = Cv_a + Cv_o + Cv_e

print('The heat capacity for zircon is: ', format(Cv, '.2f'), ' J/mol.K')

print('--------------------------------------------------------------')

########################################################################

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

print('The Debye temperature for zircon is: ', format(DTEMP, '.2f'), 'K.')

## Debye approximation of Cv and S

CON1 = 233.7818186*R
CON2 = (ITEMP**3)/(DTEMP**3)
CON3 = 77.92727286*R
CV_debye = CON1*CON2
S_debye = CON2*CON3

print('Debye approx. for the heat capacity is: ', format(CV_debye, '.2f'), ' J/mol.K')
print('Debye approx. for the entropy is: ', format(S_debye, '.2f'), ' J/K')

########################################################################
