'''
    Dada a seguinte lista:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    Faça um programa que gere uma nova lista contendo apenas números ímpares.
'''

import os

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
temp = []

while True:

    try:

        print("1) Números Par")
        print("2) Números Impar")
        acao = int(input("aguardando..\n"))

        if (acao != 2) and (acao != 1):

            ' Limpa o terminal'
            clear()

            print("Ops, sua escolha não é uma opção")
            continue

        for i in range(0, len(a)):

            if (a[i] % 2) != 0:

                if acao == 2:
                    temp.append(a[i])
            else:
                if acao == 1:
                    temp.append(a[i])

        ' Limpa o terminal'
        clear()

        print("Lista A: ", a)
        print("Números", ("Par" if (acao == 1) else "Impar") ,":", temp)
        print("____________________\n")

        ' Reseta a temp'
        temp = []

    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")