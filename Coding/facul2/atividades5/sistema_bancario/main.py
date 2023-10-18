from ContaBancaria import ContaBancaria
from ContasTipo import ContaCorrente, ContaPoupanca

conta1 = ContaCorrente('Jorge',1000, 2000) 
conta2 = ContaPoupanca ('Purcina', 5000, 0.05)

conta1.extrato()
conta1.sacar(1500)
conta1.extrato()
conta1.transferir(conta2, 500)
conta2.aplicarJuros()
conta2.extrato()