

def main_func():
    from src.tools import addition, multip,create_dict
    params = create_dict()
    print(params)
    number_1 = params['Parameter1']
    number_2 = params['Parameter2']
    print(number_1)
    print(number_2)
    dummy_addition = addition(number_1,number_2)
    dummy_multip = multip(number_1, number_2)
    text_a = 'Addition: {t1} + {t2} = {t3}'.format(t1=number_1,t2=number_2, t3=dummy_addition)
    text_m = 'Multiplication: {t1} * {t2} = {t3}'.format(t1=number_1,t2=number_2, t3=dummy_multip)
    print(text_a)
    print(text_m)




if __name__ == '__main__':
    main_func()
