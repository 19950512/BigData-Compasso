'''
    Escreva um programa que leia do teclado uma sequência de número separados por vírgula
    (e.g. 2,4,5,6,1,6) e imprime a soma de todos eles.
'''

import os

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:

        print("1) Entrar")
        print("0) Sair")
        acao = int(input("aguardando... "))

        ' Validação'
        if (acao != 1) and (acao != 0):

            ' Limpa o terminal'
            clear()

            print("Ops, sua escolha não é uma opção.")
            continue

        ' Encerrar o Software'
        if acao == 0:
            break

        ' Limpa o terminal'
        clear()

        temp = input('Informe uma sequência de números separados por vírgula: ')

        ' transforma a string em uma lista, usando a virgula como separação por linha'
        lista = list(temp.split(','))

        somaValores = 0
        for valor in range(0, len(lista)):
            somaValores += int(lista[valor])

        print("A soma da sequencia dos números é:", somaValores)

    except:

        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")