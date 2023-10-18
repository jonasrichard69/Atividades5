from ContaBancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite = 1000):
        super().__init__(titular, saldo)
        self._limite = limite

    def sacar(self, valor):
        if 0 < valor <= self._saldo + self._limite:
            self._saldo -= valor
            print (f'saque de R${valor} realizado com sucesso. ')
        else:
            print(f'saque invalido')


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo=0, taxa=0.03):
        super().__init__(titular, saldo)
        self._taxa = taxa

    def aplicarJuros(self):
        juros = self._saldo * self._taxa
        self._saldo += juros
        print (f'juros de R${juros} aplicado com sucesso.')