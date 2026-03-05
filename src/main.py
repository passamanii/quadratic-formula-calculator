from calculator import *


def main():
    
    while (True):
        try:
            a, b, c = pede_coeficientes()

            raiz1, raiz2 = calcula_raizes(a, b, c)
            print_raizes(a, b, c, raiz1, raiz2)
        
        except ValueError as error:
            print('\nErro:', error)
            continue
        
        reload = input('\nDeseja calcular mais raízes(S/N)?').upper()

        if (reload == 'N'):
            break

main()