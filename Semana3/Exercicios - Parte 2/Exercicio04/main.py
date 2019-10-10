'''
    Dada as listas a seguir:
    primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
    sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
    idades = [19, 28, 25, 31]
    Faça um programa que imprima os dados na seguinte estrutura: " - está com anos"
'''

import os

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')


' Variaveis - Default'
primeirosNomes  = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes      = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades          = [19, 28, 25, 31]

while True:

    try:

        for i in range(0 ,len(primeirosNomes)):
            print(primeirosNomes[i], sobreNomes[i], "- está com", idades[i], "anos")
        break

    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")