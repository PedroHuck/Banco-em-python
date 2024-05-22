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
numero_depositos = 0
LIMITE_SAQUES = 3
depositos = []
saques = []

while True:
    opcao = input(menu)

    if opcao == "d":
        numero = float(input("Digite quanto quer depositar: "))

        if numero < 0: 
            print("Não foi possível inserir esse valor, tente novamente.")
        else:
            numero_depositos += 1
            saldo += numero
            depositos.append(numero)

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários.")
        else:
            saque = float(input("Digite quanto quer sacar (limite de R$ 500,00): "))

            if saque > saldo:
                print("Não foi possível sacar por falta de saldo.")
            elif saque > 0 and saque <= limite:
                numero_saques += 1
                saldo -= saque
                saques.append(saque)
            else:
                print("Valor de saque inválido.")

    elif opcao == "e":
        if not depositos and not saques:
            extrato = "Não foram realizadas movimentações" 
        else:
            extrato = f"""
Depósitos: {", ".join([f"R$ {d:.2f}" for d in depositos]) if depositos else "Nenhum"}
Saques: {", ".join([f"R$ {s:.2f}" for s in saques]) if saques else "Nenhum"}
Saldo Atual: R$ {saldo:.2f}
"""
        print(extrato)

    elif opcao == "q":
        break
    else:
        print("Opção inválida. Tente novamente.")
