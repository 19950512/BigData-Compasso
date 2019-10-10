'''
    Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu
    conteúdo.
    Dica: leia documentação da função open(...),
    link: https://docs.python.org/3/library/functions.html#open
'''

import os

def ler():
    f = open("arquivo_texto.txt", "r")
    return f.read()

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:

        print("1) Ler arquivo")
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

        ' Ler o arquivo e exibir'
        print(ler())
        print("________________ F I M ______________\n")

    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")