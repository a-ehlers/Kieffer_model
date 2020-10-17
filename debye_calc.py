##################### DEBYE TEMP CALCULATION ###########################

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
