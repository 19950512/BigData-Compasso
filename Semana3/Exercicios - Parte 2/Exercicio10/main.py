'''
    Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu
    construtor, True se a lâmpada estiver ligada, False caso esteja desligada. A
    classe Lampada possuí os seguintes métodos:
        • liga(): muda o estado da lâmpada para ligada
        • desliga(): muda o estado da lâmpada para desligada
        • esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
'''

class Lampada:

    def __init__(self, status):
        self._status = status

    def esta_ligada(self):
        return self._status

    def liga(self):

        self._status = True
        return self

    def desliga(self):

        self._status = False
        return self

' Instanciamos a classe, setamos False para lampada desligada'
lampada = Lampada(False)

' Vamos ligar a lâmpada'
lampada.liga()

' Vamos ver o estado da lampada'
estado = lampada.esta_ligada()

' Vamos exibir o resultado'
print(estado)