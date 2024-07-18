from utils.menu import menu
from utils.helpers import (
    depositar,
    sacar,
    criar_conta,
    linha,
    exibir_extrato,
    listar_contas,
    criar_cliente
)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D":
            print(" Depósito ".center(50, "="))
            depositar(clientes)
            linha()

        elif opcao == "S":
            print(" Saque ".center(50, "="))
            sacar(clientes)
            linha()

        elif opcao == "E":
            print(" Extrato ".center(50, "="))
            exibir_extrato(clientes)
            linha()

        elif opcao == "Q":
            linha()
            print("Sua sessão foi encerrada. Tenha um bom dia!\n")
            break

        elif opcao == "NC":
            print(" Novo Cliente ".center(50, "="))
            criar_cliente(clientes)
            linha()

        elif opcao == "CC":
            print(" Criar Conta ".center(50, "="))
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            linha()

        elif opcao == "LC":
            print(" Listar Contas ".center(50, "="))
            listar_contas(contas)
    
        else:
            linha()
            print("Opcão Inválida!")


if __name__ == "__main__":
    main()
