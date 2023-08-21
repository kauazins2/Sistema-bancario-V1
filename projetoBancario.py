menu = """

[d] Depositar
[s] Saldo
[e] Extrato
[g] Saque
[q] Sair

=> """

saldo = 0
limite = 1500
numero_saques = 0
limite_saques = 5
extrato = ""
#definições de variáveis

while True:
#utilizaremos while pois queremos gerar um loop, onde o usuario definirá quando parar    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite um valor de deposito: "))
        
        if valor > 0:
            saldo =+ valor
            extrato += f"Depósito de R${valor: .2f}\n"
            
        else:
            print("A operação falhou")
        
        
    elif opcao == "g":
        valor = int(input("Digite um valor de saque: "))
        
        if valor > limite:
            print("Valor limite de 500, digite um valor abaixo disso")
            
        elif numero_saques > limite_saques:
            print("valor de saques excedidos")
            
        elif valor > saldo:
            print("Não há saldo suficiente")
            
        elif valor > 0:
            saldo -= valor
            print("Operação realizada com sucesso")
            extrato += f"Saque de R${valor: .2f}\n"
            numero_saques += 1

    elif opcao == "s":
        print("Seu saldo: ", saldo)
        
        
            
    
    elif opcao == "e":
        print("\n======= EXTRATO =======")
        print("Não foi realizado movimentações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=======================")
    
    elif opcao == "q":
        break    
    
    else:
        print("Comando inválido, por favor, selecione qual a operação desejada")
        