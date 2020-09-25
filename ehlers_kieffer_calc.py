## This program is hard-coded with zircon parameters

import math

## Input parameters

Vs = 3.97
Vp = 8.06
Vmax = 4.87
Vol = 130.5
Z = 2

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


########################################################################
