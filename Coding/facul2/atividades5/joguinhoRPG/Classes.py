import random
from Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, pv =100, pa=15)

    def usarSkill(self, inimigo):
        dano = random.randint(5,10)
        print(f'{self.nome} usa habilidade especial e causa {dano} de dano')
        inimigo.perderVida(dano)

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, pv =80, pa=20)

    def usarSkill(self, inimigo):
        dano = random.randint(10,20)
        print(f'{self.nome} usa habilidade especial e causa {dano} de dano')
        inimigo.perderVida(dano)

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, pv =90, pa=18)

    def usarSkill(self, inimigo):
        chance = random.random()
        if chance > 0.3:
            print(f'{self.nome} dale tiro veio')
            inimigo.perderVida(2 * self.pa)
        else:
            print(f'{self.nome} Erroooouuu')

