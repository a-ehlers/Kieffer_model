   
if __name__ == '__main__':
    from Cv_acoustic import Cv_a
    from Cv_optic import Cv_o
    from Cv_einstein import Cv_e
    #calculate heat capacity
    Cv = Cv_a + Cv_o + Cv_e
    print('The isochoric heat capacity for zircon is', Cv, 'J/mol.K')
