## Input parameters

import numpy as np

Vs = 4.8348 # kilometers/second 3.97
Vp = 8.9118 # kilometers/second 8.06
Vmax = 4.87 # kilometers/second
Vol = 130.5 # Angstroms^3
Z = 2.0 # molecules/unit cell
Natoms = 6.0 # atoms/formula unit

wc_L = 142.0 # low parameter of optic box
wc_U = 608.0 # high parameter of optic box
q_c = 0.22 # weight of optic box
wE_1 = 974.0 # first Einstein oscillator
q_1 = 0.055 # weight of first Einstein oscillator
wE_2 = 1000.0 # second Einstein oscillator
q_2 = 0.11 # weight of second Einstein oscillator
wE_3 = 885.0 # third Einstein oscillator
q_3 = 0.055 # weight of third Einstein oscillator

ITEMP = 300.0 # Kelvin

t_range_low = 20
t_range_high = 400

ATEMP = np.arange(t_range_low, t_range_high, 1)

ARRAY = ATEMP.tolist()

## Constants
AVO = 6.023e23 # 1/mole
SPEED = 3.0e10 # meters/second
BOLTZ = 1.38e-23 # Joules/Kelvin
PLANCK = 6.626e-34 # Joules.second
R = 8.3145 # Joules/mole.Kelvin
CONV = SPEED*PLANCK/BOLTZ
Vmol = Vol*0.6023/Z

## Preliminary calculations

u2 = (2./(Vs**(-3.) + Vmax**(-3.)))**(1./3.)
u1 = (1./(2.*(Vs**(-3.)) - u2**(-3.)))**(1./3.)
u3 = Vp

U_array = [u1, u2, u3] # Directionally-averaged acoustic modes
