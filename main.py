from Cv_acoustic import Cv_a
from Cv_optic import Cv_o
from Cv_einstein import Cv_e
from params import *

if __name__ == '__main__':
    #calculate heat capacity
    Cv = Cv_a + Cv_o + Cv_e
    print('The isochoric heat capacity for zircon at', ITEMP, 'K is', format(Cv, '.2f'), 'J/mol.K')
