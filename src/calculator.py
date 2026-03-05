from utils import *


def pede_coeficientes():

    while (True):
        try:
            a = test_input_error('\nInforme o valor para o coeficiente "a":')
        
            if (a == 0):
                raise ErroMatemático('O coeficiente "a" deve ser diferente de zero.')
            else:
                break
        except ErroMatemático as error:
            print('Erro:', error)
            continue
            
    b = test_input_error('Informe o valor para o coeficiente "b":')
    c = test_input_error('Informe o valor para o coeficiente "c":')

    return a, b, c

def calcula_raizes(a, b, c):

    delta = ((b**2) - (4*a*c))

    if (a == 0):
        raise ValueError('O coeficiente "a" deve ser distinto de zero.')
    if (delta < 0):
        return None, None
    
    x1 = round(((-(b)+(delta**(1/2))) / (2*a)), 4)
    x2 = round(((-(b)-(delta**(1/2))) / (2*a)), 4)

    return x1, x2

def print_raizes(a, b, c, x1, x2):

    if (x1 is None):
        print('Não existem raízes para os coeficientes dados.')
    else:
        print(f'As raízes da equação do 2º grau de coeficientes {a}, {b}, {c} são: {x1} e {x2}.')