'''
    Peça para o usuário digitar uma palavra pelo teclado e determina se a palavra digitada é ou não
    um palíndromo. Um palíndromo é uma palavra que permanece igual se lida de traz pra frente.
'''

import os

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:

        palavra = input("Informe uma palavra: ")

        ' Limpa o terminal'
        clear()

        ' Baixa a caixa para dar o mach na palavra normal e invertida (para não haver diferença entre B e b,'
        'primeira palavra maiúscula)'
        match = palavra.lower()

        if match[::-1] != match[::1]:
            print(palavra)
            print("Essa palavra NÃO É palíndromo")
        else:
            print(palavra)
            print("Essa palavra É SIM um palíndromo")

        print("____________\n")

    except:

        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")