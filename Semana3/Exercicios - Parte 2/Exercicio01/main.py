'''
    Dada duas listas como no exemplo abaixo:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Escreve um programa que retorne o que as litas têm comum (sem repetições). O seu programa
    deve funcionar para listas de qualquer tamanho.
'''

import os

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        temp = []

        for i in range(0, len(a)):

            if a[i] in b:
               temp.append(a[i])

        '''
            usa-se set para "remover" os indices duplicados e list para converter novamente para lista,
            pois o set retorna um dicionário/json
        '''
        intersecao = list(set(temp))

        print("Lista A = ", a)
        print("Lista B = ", b)
        print("Em comum = ", intersecao)
        break

    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")