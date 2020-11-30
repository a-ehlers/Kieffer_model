from params import *
import matplotlib.pyplot as plt
import numpy as np
from astropy.table import Table, Column

def heat_capacity():
    from src.Cv_acoustic import Cv_a
    from src.Cv_optic import Cv_o
    from src.Cv_einstein import Cv_e

    # initialize array of heat capacity values
    Cv = []

    for i in range(len(ATEMP)):
        Cv.append(Cv_a[i] + Cv_o[i] + Cv_e[i])

    Cv_a_percent = []
    Cv_o_percent = []
    Cv_e_percent = []
    
    for i in range(len(ATEMP)):
        Cv_a_percent.append(Cv_a[i]/Cv[i]*100)
        Cv_o_percent.append(Cv_o[i]/Cv[i]*100)
        Cv_e_percent.append(Cv_e[i]/Cv[i]*100)

##    # print table of Cv and temperature
##    Cv_table = Table([ATEMP, Cv], names = ('Temp (K)', 'Heat capacity (J/mol.K)'))
##    print(Cv_table)

    # plot Cv as a function of temp
    plt.figure(1)
    plt.plot(ARRAY, Cv_a, 'r', label='Acoustic modes')
    plt.plot(ARRAY, Cv_o, 'b', label='Optic modes')
    plt.plot(ARRAY, Cv_e, 'g', label='Einstein modes')
    plt.plot(ARRAY, Cv, 'k', label='Total heat capacity')
    plt.legend(loc='best')
    plt.title('Heat Capacity')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Contribution to Heat Capacity (J/mol.K)')
    plt.show()

    # plot Cv as a function of temp
    plt.figure(2)
    plt.plot(ARRAY, Cv_a_percent, 'r', label='Acoustic modes')
    plt.plot(ARRAY, Cv_o_percent, 'b', label='Optic modes')
    plt.plot(ARRAY, Cv_e_percent, 'g', label='Einstein modes')
    plt.legend(loc='best')
    plt.title('Heat Capacity')
    plt.xlabel('Temperature (K)')
    plt.ylabel('% Contribution to Heat Capacity (J/mol.K)')
    plt.show()

    

def internal_heat():
    from src.E_acoustic import E_a
    from src.E_optic import E_o
    from src.E_einstein import E_e

    # initialize array of internal heat values
    E = []

    for i in range(len(ATEMP)):
        E.append(E_a[i] + E_o[i] + E_e[i])

    # plot E as a function of temp
    plt.figure(3)
    plt.plot(ARRAY, E_a, 'r', label='Acoustic modes')
    plt.plot(ARRAY, E_o, 'b', label='Optic modes')
    plt.plot(ARRAY, E_e, 'g', label='Einstein modes')
    plt.plot(ARRAY, E, 'k', label='Total internal heat')
    plt.legend(loc='best')
    plt.title('Internal Energy')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Contribution to Internal Energy (J)')
    plt.show()

def entropy():
    from src.S_acoustic import S_a
    from src.S_optic import S_o
    from src.S_einstein import S_e

    # initialize array of entropy values
    S = []

    for i in range(len(ATEMP)):
        S.append(S_a[i] + S_o[i] + S_e[i])

    S_table = Table([ATEMP, S], names = ('Temp (K)', 'Entropy (J/K)'))
    print(S_table)

    # plot entropy as a function of temp
    plt.figure(4)
    plt.plot(ARRAY, S_a, 'r', label='Acoustic modes')
    plt.plot(ARRAY, S_o, 'b', label='Optic modes')
    plt.plot(ARRAY, S_e, 'g', label='Einstein modes')
    plt.plot(ARRAY, S, 'k', label='Total entropy')
    plt.legend(loc='best')
    plt.title('Entropy')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Contribution to Entropy (J/K)')
    plt.show()

def helmholtz():
    from src.F_acoustic import F_a
    from src.F_optic import F_o
    from src.F_einstein import F_e

    # initialize array of free energy values
    F = []

    for i in range(len(ATEMP)):
        F.append(F_a[i] + F_o[i] + F_e[i])

    # plot free energy as a function of temp
    plt.figure(5)
    plt.plot(ARRAY, F_a, 'r', label='Acoustic modes')
    plt.plot(ARRAY, F_o, 'b', label='Optic modes')
    plt.plot(ARRAY, F_e, 'g', label='Einstein modes')
    plt.plot(ARRAY, F, 'k', label='Total entropy')
    plt.legend(loc='best')
    plt.title('Helmholtz Free Energy')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Contribution to Helmholtz free energy (J)')
    plt.show()

if __name__ == '__main__':
    heat_capacity()
##    internal_heat()
##    entropy()
##    helmholtz()
