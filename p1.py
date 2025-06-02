'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para: preti.joao@ifmt.edu.br
Assunto: Prova 1 de Laboratório de Programação 2025/1
Mensagem: Coloque seu nome completo na mensagem do e-mail
Anexo: prova.py
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

#1. Faça um programa que leia o saldo de uma conta corrente,
#   o juros de rendimento mensal e imprima o valor em reais do
#   rendimento referente a 1 mês de juros. (2,5pt)
def q1():
    saldo = input_float('Saldo: R$ ',0,1_000_000_000)
    try:
        juros = float(input('Juros: '))
    except ValueError:
        print('O juros informado não é um número Real!')
    try:
        print(f'Rendimento 1 mês: {saldo*juros/100}')
    except UnboundLocalError:
        print('Como o saldo ou juros não foi informado corretamente, o rendimento não pode ser calculado!')
q1()
#2. Complemente a questão 1 da prova, para que o cálculo do
#   rendimento só ocorra se o saldo da conta for positivo.
#   Caso contrário, deverá exibir uma mensagem informando que o
#   rendimento não pode ser calculado para valores negativos ou sem
#   saldo em conta corrente. (2,5pt)
def q2():
    saldo = float(input('Saldo: R$ '))
    juros = float(input('Juros: '))
    if saldo >= 0:
        print(f'Rendimento 1 mês: {saldo*juros/100}')
    else:
        print('Saldo negativo, não possui rendimento!')

#3. Complemente a questão 1 ou 2 da prova, para que não seja aceito juros
#   negativo. O programa deve reiteradamente informar o usuário do erro
#   e solicitar novo valor para o juros. (2,5pt)
def q3():
    saldo = float(input('Saldo: R$ '))
    juros = -1
    while juros < 0:
        juros = float(input('Juros: '))
    print(f'Rendimento 1 mês: {saldo*juros/100}')

#4. Complemente a questão 1, 2 ou 3 da prova, para que o cálculo
#    do rendimento suporte um prazo maior do que 1 mês. (2,5pt)
#    O programa deverá solicitar do usuário também prazo do
#    investimento em meses.
#    Atenção: trata-se de uma operação de juros composto.
def q4():
    saldo = float(input('Saldo: R$ '))
    juros = float(input('Juros: '))
    prazo = int(input('Prazo em meses: '))
    for _ in range(prazo):
        saldo += saldo*juros/100 
    print(f'Saldo atualizado após {prazo} meses: {saldo}')    