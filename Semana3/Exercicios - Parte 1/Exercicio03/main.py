'''
    Escreva um código Python que imprime os números pares de 0 até 20 (incluso).
    Dica: olhe a documentação da função range(). Mais informações no link
'''

import os

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:

        print("1) Números Par")
        print("2) Números Impar")
        acao = int(input("aguardando..\n"))

        if (acao != 2) and (acao != 1):
            print("Ops, sua escolha não é uma opção")
            continue

        print("-Números PAR-" if (acao == 1) else "- Números IMPAR-")
        for i in range(0, 21):

            if (i % 2) == 0:

                'Números Pares'
                if acao == 1:
                    print(i)
            else:

                if acao == 2:
                    'Números Impares'
                    print(i)

        print("__________________\n")

    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")