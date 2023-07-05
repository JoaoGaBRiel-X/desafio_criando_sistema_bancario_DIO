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
        valor_deposito = int(input("Digite o valor do depósito: "))

        if valor_deposito <= 0:
            print("Valor inválido!")
            print("Por favor, refaça a operação")
        else:
            extrato += f"\nDepósito de R$ {valor_deposito:.2f}"
            saldo += valor_deposito
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com Sucesso!")

    elif opcao == "s":
        valor_saque = int(input("Digite o valor do saque: "))
        if valor_saque <= 0:
            print("Valor inválido!")
            print("Por favor, refaça a operação")
        else:
            if numero_saques < LIMITE_SAQUES:
                if valor_saque <= saldo:
                    if valor_saque <= limite:
                        extrato += f"\nSaque de R$ {valor_saque:.2f}"
                        saldo -= valor_saque
                        numero_saques += 1
                        print(f"Saque de R$ {valor_saque:.2f} realizado com Sucesso!")
                    else:
                        print("OPERAÇÃO CANCELADA!")
                        print(f"Valor de R$ {valor_saque:.2f} excede o limite liberado de R$ {limite:.2f} por operação.")
                else:
                    print("OPERAÇÃO CANCELADA!")
                    print(f"Saldo insuficiente para realizar operação.")
                    print(f"Saldo atual é de R$ {saldo:.2f}")
            else:
                print("OPERAÇÃO CANCELADA!")
                print(f"Limite diário de {LIMITE_SAQUES} saques foi atingido!")

    elif opcao == "e":
        print("*************** EXTRATO ***************")
        print("Sem movimentação." if not extrato else extrato)
        print(f"\nSALDO ATUAL R$ {saldo:.2f}")
        print("***************************************")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")