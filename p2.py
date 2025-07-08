'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para: preti.joao@ifmt.edu.br
Assunto: Prova 2 de Laboratório de Programação 2025/1
Mensagem: Coloque seu nome completo na mensagem do e-mail
Anexo: prova2.py
'''
import random
#1. Faça um programa que gere aleatoriamente 15 números inteiros em uma lista
#   e depois permita que o usuário digite um número inteiro para ser buscado
#   na lista, se for encontrado o programa deve imprimir a posição desse
#   número na lista, caso contrário, deve imprimir a mensagem: "Não encontrado!".
#   (2,5pt)
def q1():
    lista = [random.randint(0, 100) for _ in range(15)]
    print(lista)
    num = int(input('Número a ser localizado: '))
    if num in lista:
        print(lista.index(num))
    else:
        print('Número não localizado!')

#2. Complemente a questão 1 sem utilizar o recurso de ordenação. O programa
#   deve  imprimir ao final: o maior e o menor número da lista, o percentual
#   de números pares e a média dos elementos da lista. (2,5pt)
def q2():
    lista = [random.randint(0, 100) for _ in range(15)]
    print(lista)
    maior = 0
    menor = 101
    pares = 0
    soma = 0
    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        if num % 2 == 0:
            pares += 1
        soma += num
    resultado = f'''
    Maior: {maior}
    Menor: {menor}
    Percentual de Pares: {pares/15*100}%
    Média: {soma/15}
    '''
    print(resultado)

#3. Altere a questão 1 ou 2 da prova, para que os 15 números da lista não sejam
#   mais aleatórios, e sim provenientes de um arquivo de nome "entrada.csv", cuja
#   primeira e única linha do arquivo, contenha os 15 números separados por
#   ponto e vírgula (;). (2,5pt)
def q3():
    lista = []
    arq = open('entrada.csv','r')
    for linha in arq:
        lista = linha.split(';')
    print(lista)
    num = input('Número a ser localizado: ')
    if num in lista:
        print(lista.index(num))
    else:
        print('Número não localizado!') 

#4. Complemente a questão 1, 2 ou 3 da prova, para que o resultado apresentado
#   em tela, seja gravado em um arquivo de nome "resultado.txt". (2,5pt)
def q4():
    lista = [random.randint(0, 100) for _ in range(15)]
    print(lista)
    maior = 0
    menor = 101
    pares = 0
    soma = 0
    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        if num % 2 == 0:
            pares += 1
        soma += num
    resultado = f'''
    Maior: {maior}
    Menor: {menor}
    Percentual de Pares: {pares/15*100}%
    Média: {soma/15}
    '''
    arq = open('resultado.txt','w')
    arq.write(resultado)
    arq.close()
