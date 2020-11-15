from params import *
import matplotlib.pyplot as plt
import numpy as np
##import matplotlib.pyplot as plt

def heat_capacity():
    from src.Cv_acoustic import Cv_a
    from src.Cv_optic import Cv_o
    from src.Cv_einstein import Cv_e
    
    Cv = []

    for i in range(len(ATEMP)):
        Cv.append(Cv_a[i] + Cv_o[i] + Cv_e[i])

    plt.figure(1)
    plt.plot(ARRAY, Cv_a, 'r', label='acoustic modes')
    plt.plot(ARRAY, Cv_o, 'b', label='optic modes')
    plt.plot(ARRAY, Cv_e, 'g', label='einstein modes')
    plt.plot(ARRAY, Cv, 'k', label='total heat capacity')
    plt.legend(loc="best")
    plt.title('Heat Capacity')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Contribution to Heat Capacity (J/mol.K)')
    plt.show()

def internal_heat():
    from src.E_acoustic import E_a
    from src.E_optic import E_o
    from src.E_einstein import E_e

    E = []

    for i in range(len(ATEMP)):
        E.append(E_a[i] + E_o[i] + E_e[i])

    plt.figure(2)
    plt.plot(ARRAY, E_a, 'r', label='acoustic modes')
    plt.plot(ARRAY, E_o, 'b', label='optic modes')
    plt.plot(ARRAY, E_e, 'g', label='einstein modes')
    plt.plot(ARRAY, E, 'k', label='total internal heat')
    plt.legend(loc="best")
    plt.title('Internal Energy')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Contribution to Internal Energy (J)')
    plt.show()

def entropy():
    from src.S_acoustic import S_a
    from src.S_optic import S_o
    from src.S_einstein import S_e

    S = []

    for i in range(len(ATEMP)):
        S.append(S_a[i] + S_o[i] + S_e[i])

    plt.figure(3)
    plt.plot(ARRAY, S_a, 'r', label='acoustic modes')
    plt.plot(ARRAY, S_o, 'b', label='optic modes')
    plt.plot(ARRAY, S_e, 'g', label='einstein modes')
    plt.plot(ARRAY, S, 'k', label='total entropy')
    plt.legend(loc="best")
    plt.title('Entropy')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Contribution to Entropy (J/K)')
    plt.show()

def helmholtz():
    from src.F_acoustic import F_a
    from src.F_optic import F_o
    from src.F_einstein import F_e

    F = []

    for i in range(len(ATEMP)):
        F.append(F_a[i] + F_o[i] + F_e[i])

    plt.figure(4)
    plt.plot(ARRAY, F_a, 'r', label='acoustic modes')
    plt.plot(ARRAY, F_o, 'b', label='optic modes')
    plt.plot(ARRAY, F_e, 'g', label='einstein modes')
    plt.plot(ARRAY, F, 'k', label='total entropy')
    plt.legend(loc="best")
    plt.title('Helmholtz Free Energy')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Contribution to Helmholtz free energy (J)')
    plt.show()

if __name__ == '__main__':
    heat_capacity()
    internal_heat()
    entropy()
    helmholtz()
