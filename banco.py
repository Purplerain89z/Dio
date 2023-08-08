def menu():
    menu = """\n
    ============================ MENU ============================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNovo Conta
    [lc]\tLista de Contas
    [nu]\tNovo Usuario
    [q]\tSair
    => """
    return menu

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n====Depósito realizado com sucesso! ====")
    else:
        print("\n@@@ operação falhou! O valor informado é inválido. tente novamente. @@@")    

    return saldo, extrato    

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saques

    if excedeu_saldo:
        print ("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor de saque excede o limite. @@@")    

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")    

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saque += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@') 

    return saldo, extrato           

def exibir_extrato(saldo, /, *, extrato):
        print("\n======================EXTRATO======================")
        print("Não foram realizadas movimentaçãos." if not extrato else extrato)
        print(f"\nSaldo:R$' {saldo:.2f}")
        print("======================================================") 

def criar_usuario(usuarios):
    cpf = input("informar o CPF(somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ CPF já cadastrado certifique que digitou corretamente! @@@")
        return
    
    nome =input("Informe o nome completo: ")
    data_nascimento = input("informe a data de nascimento(dd-mm-aaaa):")
    endereco = input("informe o endereço(logradouro, numero - bairro - cidade/sigla do estado): ")

    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "CPF": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtratos = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtratos[0] if usuarios_filtratos else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):    
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)       

def main():
 
 LIMITE_SAQUES = 3
 AGENCIA = "0001"

 saldo = 0
 limite = 500
 extrato = ""
 numero_saques = 0
 usuarios = []
 contas = []

 while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == 'lc':
        listar_contas(contas)    

    elif opcao == 'nu':
       criar_usuario(usuarios)      

    elif opcao == "q":
        print("Voltando a tela inicial")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")