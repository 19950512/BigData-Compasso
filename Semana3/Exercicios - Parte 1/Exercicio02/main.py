'''
    Escreva um código Python que lê do teclado um número digitado pelo usuário e imprime se ele
    par ou ímpar.
'''

import os

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:

        numero = int(input("Informe um número: "))

        resposta = "O número '" + str(numero) + "' é impar"

        if (numero % 2) == 0:
            resposta = "O número '" + str(numero) + "' é par"

        ' Limpa o terminal'
        clear()
        print(resposta)
        print("____________________\n\n\n")

    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")