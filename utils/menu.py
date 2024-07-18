def menu():
    menu = """
    ===================== MENU ====================

    Escolha a opção desejada

    [NC] Novo Cliente
    [CC] Criar Conta
    [LC] Listar Contas
    [D ] Depósito
    [S ] Saque
    [E ] Extrato
    [Q ] Sair

    """
    return input(menu).upper()
