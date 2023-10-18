from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto

def acelerar(veiculo, aumento):
    veiculo.acelerar(aumento)

carro1 = Carro ("Corsa", 82, "automatico")
moto1 = Moto ("CG", 2012, "manual")

carro1.andar()
carro1.trocarMarcha()
moto1.andar()
moto1.trocarMarcha()

carro1.descricao()
moto1.descricao()

acelerar(carro1, 20)
carro1.andar()

acelerar(moto1, 50)
moto1.andar()
