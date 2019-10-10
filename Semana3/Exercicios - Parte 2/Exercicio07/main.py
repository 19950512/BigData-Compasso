'''
    Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
    Dica: leia a documentação do pacote json, link: https://docs.python.org/3/library/json.html
'''

import os
import json

def ler(arquivo):

    if os.path.isfile(arquivo):
        f = open(arquivo, "r")
        return f.read()

    return "Arquivo não encontrado."

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

Arquivo = "person.json"

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

        arquivo = ler(Arquivo)
        valor = json.loads(arquivo)

        for indice in valor:
            print(indice,"=",valor[indice])
        print("________________ F I M ______________\n")


    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")