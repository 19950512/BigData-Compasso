'''
    Texto aqui
'''

import os

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:

        print("1) Primeira Opção")
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

        '''
            DAQUI PARA BAIXO, VAI A LÓGICA 
        '''

    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")