'''
    Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma
    função como segundo argumento. Esta função aplica a função recebida para cada elemento da
    lista recebida retorna o resultado em uma nova lista.
    Teste sua função para saber se está ok.
'''

def minha_funcao(valor):
    return (valor * valor) * -1

def my_map(lista, qualquer_outra_funcao):
    temp = []
    for i in range(0, len(lista)):
        temp.append(qualquer_outra_funcao(lista[i]))

    return temp


Lista_Primaria = [4, 2, 3]

Lista_Processada = my_map(Lista_Primaria, minha_funcao)

print("Lista Original:", Lista_Primaria)
print("Lista Processada:", Lista_Processada)