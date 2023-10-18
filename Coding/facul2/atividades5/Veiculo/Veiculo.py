class Veiculo():
    def __init__(self, tipo, velocidade):
        self._tipo = tipo
        self._velocidade = velocidade

    def especificar (self):
        print (f'é um {self._tipo} e anda a aproximadamente a {self._velocidade}')

    def acelerar(self, aumento):
        self._velocidade += aumento

        