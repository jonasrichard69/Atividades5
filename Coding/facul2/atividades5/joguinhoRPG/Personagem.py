import random

#pv= pontos de vida, pa= pontos de ataque, pd= pontos de dano
class Personagem:
    def __init__(self, nome, pv, pa):
        self.nome= nome
        self. __pv = pv
        self.pa = pa

    def atacar (self, inimigo):
        print(f'{self.nome} ataca')
        inimigo.perderVida(self.pa)
    
    def perderVida(self, pd):
        self.__pv -= pd
        if self.__pv <= 0:
            self.__pv = 0

    def estaVivo(self):
        return self.__pv >0
    
    def mostrarStatus(self):
        print(f'{self.nome}: PV - {self.__pv}, PA - {self.pa}')