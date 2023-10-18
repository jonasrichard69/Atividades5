from Personagem import Personagem
from Classes import Guerreiro, Mago, Arqueiro

def combate(personagem1, personagem2):
    print('--------------')
    personagem1.mostrarStatus()
    personagem2.mostrarStatus()
    print('--------------')
    while personagem1.estaVivo() and personagem2.estaVivo():
        personagem1.atacar(personagem2)
        personagem2.mostrarStatus()
        personagem2.atacar(personagem1)
        personagem1.mostrarStatus()
        print('--------------')
        personagem1.usarSkill(personagem2)
        personagem2.mostrarStatus()
        personagem2.usarSkill(personagem1)
        personagem1.mostrarStatus()
        print('--------------')
        

guerreiro = Guerreiro('Rogerio Ceni')
mago = Mago ('Donald Tramp')
arqueiro = Arqueiro('Faustao')

combate(guerreiro, arqueiro)
print('\n --- proximo combate --- \n')