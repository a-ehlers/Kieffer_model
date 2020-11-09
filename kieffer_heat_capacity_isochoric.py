## This program is hard-coded with zircon parameters

import math
from scipy.integrate import quad

## Input parameters

Vs = 3.97 # kilometers/second
Vp = 8.06 # kilometers/second
Vmax = 4.87 # kilometers/second
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

ITEMP = 1000 # Kelvin

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

##print(X_array)

acoustic=[]

for i in X_array:
    # integrate acoustic function
    result,error = quad(lambda x: ((math.asin(x/i)**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(i**2.-x**2)*((math.exp(x))-1.)**2.)
, 0, i)

<<<<<<< HEAD
    acoustic.append(result)
=======

dummy = default_value
for i in range(3)
    dummy+= integrand(dummy)
SUM = dummy

SUM1 = quad(integrand, 0, acoustic_1)
>>>>>>> b1d28d5c8fc1d3aacbf55ae7e39ee4f86d9a851f

print(acoustic)

SUM = acoustic[0]+acoustic[1]+acoustic[2]

Cv_a = (3.*AVO*BOLTZ*SUM/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)

print('Contribution from acoustic modes to Cv: ', format(Cv_a, '.2f'), ' J/mol.K')
########################################################################

########################### OPTIC BOX ##################################

# f is Gaussian quadrature function: x^2*exp(x)/(xU-xL)*(exp(x)-1)^2

x_L = wc_L*CONV/ITEMP

x_U = wc_U*CONV/ITEMP

##print(x_L, x_U)

f = lambda X: ((x_U-x_L)/2.)*(((((x_U-x_L)*X+x_U+x_L)/2.)**2.*math.exp(((x_U-x_L)* \
             X+x_U+x_L)/2.))/((x_U - x_L)*(math.exp(((x_U-x_L)*X+x_U+x_L)/2.)-1)**2.))

##quad_2 = f(-math.sqrt(1/3)) + f(math.sqrt(1/3))

quad_3 = (5./9.)*f(-math.sqrt(0.6)) + (8./9.)*f(0) + (5./9.)*f(math.sqrt(0.6))

##print(quad_3)

Cv_o = 3.*AVO*BOLTZ*(1-1./(Natoms*Z)-q_c)*quad_3

print('Contribution from optic box to Cv: ', format(Cv_o, '.2f'), ' J/mol.K')
########################################################################

######################## EINSTEIN OSCILLATORS ##########################

WE_array = [wE_1, wE_2, wE_3]

ein_array = []

for i in WE_array:
    ein_array.append(((i*CONV/ITEMP) \
    **2.0*math.exp(i*CONV/ITEMP))/((math.exp(i*CONV/ITEMP)-1)**2.0))

Cv_e = 3.*AVO*BOLTZ*(q_1*ein_array[0] + q_2*ein_array[1] + q_3*ein_array[2])

print('Contribution from Einstein oscillators to Cv: ', format(Cv_e, '.2f'), ' J/mol.K')

Cv = Cv_a + Cv_o + Cv_e

print('The isochoric heat capacity for zircon at ', ITEMP, ' K is:', format(Cv, '.2f'), ' J/mol.K')

########################################################################
