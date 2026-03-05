class ErroMatemático(Exception):
    pass


def test_input_error(mensagem):
    
    while (True):
        try: 
            num = float(input(mensagem))
            return num
        except ValueError:
            print('Insira um número válido.')