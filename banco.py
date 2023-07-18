menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}"
        else:
             print("Operação falhou! Valor inválido tenten novamente ou pessa ajuda a um dos funcionarios.")    

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo    
        exedeu_limite = valor > limite
        exedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente, verifique seu extrato e tente novamente.")      
        elif exedeu_limite:
            print("Limite do dia para saques excedido, tente amanhã.")
        elif exedeu_saques:
            print("O numero de saques exedidos para hoje, tente amanhã")    
        elif valor > 0:
            saldo -= valor
            extrato += f"saque:RS{valor:.2f}\n"
            numero_saques +=1    

        else:
            print("Operação inválida, tente novamente.")    

            
    elif opcao == "e":
        print("\n======================EXTRATO======================")
        print("Não foram realizadas movimentaçãos." if not extrato else extrato)
        print(f"\nSaldo:R$' {saldo:.2f}")
        print("======================================================")
    
    elif opcao == "q":    
        break     

    else:
            print("Operação Inválida, por favor selecione novamente a operação desejada.")