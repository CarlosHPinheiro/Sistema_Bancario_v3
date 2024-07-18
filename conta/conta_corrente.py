from conta.conta import Conta
from transacao.saque import Saque

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=1000, limite_saques=5):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques 

        if excedeu_limite:
            print("Operação Falhou! Valor acima do limite permitido!")

        elif excedeu_saques:
            print("Operação Falhou! Limite de Saques atingido!")

        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
            Agência:\t {self.agencia}
            C/C:    \t {self.numero}
            Titular:\t {self.cliente.nome}
            """
