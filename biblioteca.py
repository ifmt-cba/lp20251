import random
'''
Funções úteis para diversos programas
'''
def input_float(msg, min, max):
    error = True
    numero = 0
    while error == True:
        try:
            numero = float(input(msg))
            if numero < min or numero > max:
                print(f'Valor informado fora do intervalo permitido {min}-{max}')
            else:
                error = False
        except ValueError:
            print('O valor informado não é um número Real!')
        except:
            print('Erro desconhecido. Entre em contato com o admin do sistema!')
    return numero

def input_int(msg, min, max):
    error = True
    numero = 0
    while error == True:
        try:
            numero = int(input(msg))
            if numero < min or numero > max:
                print(f'Valor informado fora do intervalo permitido {min}-{max}')
            else:
                error = False
        except ValueError:
            print('O valor informado não é um número Inteiro!')
        except:
            print('Erro desconhecido. Entre em contato com o admin do sistema!')
    return numero

def nomeAleatorio():
    nomes = ['João', 'Pedro','Carla', 'Maria', 'José', 'Ana']
    return nomes[random.randrange(0,6)]