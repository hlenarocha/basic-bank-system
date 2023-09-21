LIMITE_SAQUE = float(500)
LIMITE_SAQUE_DIA = 3
saldo = float(3000)

saques_realizados = []
depositos_realizados = []

while True:
    menu = '''
---------------DIO BANK---------------
Bem-vindo (a) ao DIO BANK System!

Escolha a operação que deseja efetuar:
[1] SAQUE
[2] DEPÓSITO
[3] EXTRATO
[0] SAIR
--------------------------------------
'''
    operacao = input(menu)

    if operacao == "1":
        total_saques = 0
        saque = float(input('''
-----------------SAQUE-----------------
Informe o valor do saque ou digite 0 
para encerrar a operação: 
---------------------------------------\n'''))
        while saque != 0:
            if saque > LIMITE_SAQUE: 
                print(f"Operação não efetuada: limite de R${LIMITE_SAQUE:.2f} por saque atingido!")
            elif total_saques >= LIMITE_SAQUE_DIA:
                print(f"Operação não efetuada: limite de {LIMITE_SAQUE_DIA} saques diários atingido!")
            else:
                if saque > 0:
                    print(f'''
Realizando saque de R${saque:.2f}...
Retire o dinheiro no caixa eletrônico.''')
                    saldo -= saque
                    saques_realizados.append(saque)
                    total_saques = len(saques_realizados)
            saque = float(input('''
-----------------SAQUE-----------------
Informe o valor do saque ou digite 0 
para encerrar a operação: 
---------------------------------------\n'''))

    elif operacao == "2":
        deposito = float(input('''
----------------DEPÓSITO----------------
Informe o valor do depósito ou
digite 0 para encerrar operação: 
----------------------------------------\n'''))
        while deposito != 0: 
            if deposito > 0:
                print(f'''
Realizando depósito de R${deposito:.2f}...
Depósito efetuado com sucesso!''')
                saldo += deposito
                depositos_realizados.append(deposito)
                total_depositos = len(depositos_realizados)
            deposito = float(input('''
----------------DEPÓSITO----------------
Informe o valor do depósito ou
digite 0 para encerrar operação: 
----------------------------------------\n'''))

    elif operacao == "3":
        numero_saque = 1
        numero_deposito = 1
        print("EXTRATO".center(38, "-"))
        print()
        print(f"SALDO: R${saldo:.2f}\n")

        print("SAQUES: \n")
        if not saques_realizados:
            print("Nenhum saque efetuado.\n")
        else:
            for cada_saque in saques_realizados:
               print(f"SAQUE {numero_saque} --------- R${cada_saque:.2f}\n")
               numero_saque += 1
        print()
        print("DEPÓSITOS: \n")
        if not depositos_realizados:
                print("Nenhum depósito efetuado.\n")
        else:
               for cada_deposito in depositos_realizados:
                   print(f"DEPÓSITO {numero_deposito} ------- R${cada_deposito:.2f}\n")
                   numero_deposito += 1
        print("--------------------------------------")
        input("\nPressione ENTER para retornar ao menu.")
    
    elif operacao == "0":
        print("Encerrando o programa...\nObrigado por utilizar o DIO BANK System!")
        break

    else:
        print("Nenhuma operação selecionada. Escolha uma operação válida: ")
