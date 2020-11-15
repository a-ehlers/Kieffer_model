## Calculation of acoustic mode contributions to heat capacity (Cv)

import math
import numpy as np
from scipy.integrate import quad

#import params.py for all input parameters
from params import *

########################### ACOUSTIC MODES ###############################
##
##u2 = (2./(Vs**(-3.) + Vmax**(-3.)))**(1./3.)
##u1 = (1./(2.*(Vs**(-3.)) - u2**(-3.)))**(1./3.)
##u3 = Vp
##
##U_array = [u1, u2, u3] # Directionally-averaged acoustic modes
##X_array = [] # Nondimensionalized branches
##
##Vmol = Vol*0.6023/Z
##
####Kmax = (6.*(math.pi)*(math.pi)*(10**24)/Vol)**1./3.
##
##for i in U_array:
##    X_array.append((132.32*i/(Vol**(1./3.)))*CONV/ITEMP)
##
##acoustic=[]
##
##for i in X_array:
##    # integrate acoustic function
##    result_acoustic,error_acoustic = quad(lambda x: ((math.asin(x/i)**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(i**2.-x**2)*((math.exp(x))-1.)**2.)
##, 0., i)
##
##    acoustic.append(result_acoustic)
##
##
####def acoustic(x):
####    for i in X_array:
####        return ((math.asin(x/i)**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(i**2.-x**2)*((math.exp(x))-1.)**2.)
##        
##
##Cv_a = (3.*AVO*BOLTZ*(acoustic[0]+acoustic[1]+acoustic[2])/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)
##
##print('Contribution from acoustic modes to Cv: ', format(Cv_a, '.2f'), ' J/mol.K')
##########################################################################

u2 = (2./(Vs**(-3.) + Vmax**(-3.)))**(1./3.)
u1 = (1./(2.*(Vs**(-3.)) - u2**(-3.)))**(1./3.)
u3 = Vp

U_array = [u1, u2, u3] # Directionally-averaged acoustic modes

Vmol = Vol*0.6023/Z

Cv_a = []

##X_array = [0.5, 0.6, 1]

for i in ATEMP:
    X_array = [] # Nondimensionalized branches
    for j in U_array:
        X_array.append((132.32*j/(Vol**(1./3.)))*CONV/i)
        
    acoustic = []

    def acoustic_0(x):
        return ((math.asin(x/X_array[0])**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(X_array[0]**2.-x**2)*((math.exp(x))-1.)**2.)
    
    acoustic_quad_0, error = quad(acoustic_0, 0, X_array[0])
    acoustic.append(acoustic_quad_0)

    def acoustic_1(x):
        return ((math.asin(x/X_array[1])**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(X_array[1]**2.-x**2)*((math.exp(x))-1.)**2.)
    
    acoustic_quad_1, error = quad(acoustic_1, 0, X_array[1])
    acoustic.append(acoustic_quad_1)

    def acoustic_2(x):
        return ((math.asin(x/X_array[2])**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(X_array[2]**2.-x**2)*((math.exp(x))-1.)**2.)
    
    acoustic_quad_2, error = quad(acoustic_2, 0, X_array[2])

    acoustic.append(acoustic_quad_2)
    acoustic_Cv = (3.*AVO*BOLTZ*(acoustic[0]+acoustic[1]+acoustic[2])/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)
    Cv_a.append(acoustic_Cv)

##print(Cv_a)

##for i in ATEMP:
##    for j in U_array:
##        X_array.append((132.32*j/(Vol**(1./3.)))*CONV/i)
##        
##    acoustic = []
##
##    for k in X_array:
##        result_acoustic,error_acoustic = quad(lambda x: ((math.asin(x/k)**2.)*(x**2.)*(math.exp(x)))/(math.sqrt(k**2.-x**2)*((math.exp(x))-1.)**2.), 0., k)
##
##        acoustic.append(result_acoustic)
##
##    acoustic_Cv = (3.*AVO*BOLTZ*(acoustic[0]+acoustic[1]+acoustic[2])/(Natoms*Z))*(2./math.pi)*(2./math.pi)*(2./math.pi)
##
##    Cv_a.append(acoustic_Cv)
##
####print(Cv_a)

