import textwrap
from transacao.deposito import Deposito
from transacao.saque import Saque
from cliente.pessoa_fisica import PessoaFisica
from conta.conta_corrente import ContaCorrente

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
    

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui contas!")
        return
    
    return cliente.contas[0]


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado! Operação encerrada!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!")


def linha():
    print("=" * 50)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    transacoes = conta.historico.transacoes
    
    extrato = ""

    if not transacoes:
        extrato = "Não foram realizadas movimentações."

    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")


def listar_contas(contas):
    for conta in contas:
        linha()
        print(textwrap.dedent(str(conta)))


def criar_cliente(clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Cliente já existe!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Logradouro, n°- Bairro - Cidade/UF : ")

    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)

    clientes.append(cliente)

    print("\nCadastro realizado com sucesso!")
