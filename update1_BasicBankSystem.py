import textwrap
import time

LIMITE_SAQUES_DIA = 3
LIMITE_SAQUE = float(1000)
AGENCIA = "0001"
valor = 0
saques_realizados = []
depositos_realizados = []
usuarios = []
contas = []

def menu():
    menu = '''
    ---------------BANK-------------------
    Bem-vindo (a) ao BANK System!

    Escolha a operação que deseja efetuar:
    [1] SAQUE
    [2] DEPÓSITO
    [3] EXTRATO
    [4] NOVA CONTA
    [5] LISTAR CONTAS
    [6] NOVO USUÁRIO
    [0] SAIR
    --------------------------------------
    ==> '''
    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, LIMITE_SAQUES_DIA, LIMITE_SAQUE): #keyword only *
    valor = float(input('''
-----------------SAQUE-----------------
Informe o valor do saque ou digite 0 
para encerrar a operação: 
---------------------------------------\n'''))
    while valor != 0:
        total_saques = len([extrato for op in extrato if op < 0])
        if valor > LIMITE_SAQUE: 
            print(f"Operação não efetuada: limite de R${LIMITE_SAQUE:.2f} por saque atingido!")
        elif total_saques >= LIMITE_SAQUES_DIA:
            print(f"Operação não efetuada: limite de {LIMITE_SAQUES_DIA} saques diários atingido!")
        elif saldo < valor:
            print("Operação não efetuada: saldo insuficiente!")
        else:
            if valor > 0:
                print(f'''
Realizando saque de R${valor:.2f}...
Retire o dinheiro no caixa eletrônico.''')
                saldo -= valor
                extrato.append(-valor)

        valor = float(input('''
-----------------SAQUE-----------------
Informe o valor do saque ou digite 0 
para encerrar a operação: 
---------------------------------------\n'''))
    return saldo, extrato
    
def deposito(saldo, valor, extrato, /): #positional only /
    valor = float(input('''
----------------DEPÓSITO----------------
Informe o valor do depósito ou
digite 0 para encerrar operação: 
----------------------------------------\n'''))
    while valor != 0: 
        if valor > 0:
            print(f'''
Realizando depósito de R${valor:.2f}...
Depósito efetuado com sucesso!''')
            saldo += valor
            extrato.append(valor)
        valor = float(input('''
----------------DEPÓSITO----------------
Informe o valor do depósito ou
digite 0 para encerrar operação: 
----------------------------------------\n'''))
    return saldo, extrato 

def extrato(saldo, /, *, extrato):
    print("EXTRATO".center(38, "-"))
    print()
    print(f"SALDO: R${saldo:.2f}\n")

    if not extrato:
        print("Não foram realizadas movimentações nesta conta.\n")
    
    saques_realizados = []
    depositos_realizados= []
    for valor in extrato:
        if valor > 0:
            depositos_realizados.append(valor)
        else:
            saques_realizados.append(-valor)
    print("SAQUES: ")
    if not saques_realizados:
        print("Nenhum saque efetuado.")

    else:
        numero_saque = 1
        for cada_saque in saques_realizados:
            print(f"SAQUE {numero_saque} --------- R${cada_saque:.2f}\n")
            numero_saque += 1

    print("DEPÓSITOS: ")
    if not depositos_realizados:
        print("Nenhum depósito efetuado.\n")
    else:
        numero_deposito = 1
        for cada_deposito in depositos_realizados:
            print(f"DEPÓSITO {numero_deposito} ------- R${cada_deposito:.2f}\n")
            numero_deposito += 1
        print("--------------------------------------")
        input("\nPressione ENTER para retornar ao menu.")

def nova_conta(agencia, numero_conta, usuarios):
    print("NOVA CONTA".center(38, "-"))
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtro_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo":0, "extrato":[]}
    
    print("Usuário não encontrado. Selecione a operação [6] \npara criar um novo usuário e, posteriormente, \numa nova conta [4].")

def listar_contas(contas):
    for conta in contas:
        linha = f'''
    Agência:\t{conta['agencia']}
    C/C:\t{conta['numero_conta']}
    Titular:\t{conta['usuario']['nome']}'''
        print(linha)
    if len(contas) == 0:
        print("Nenhuma conta criada.\n")
    time.sleep(2)

def novo_usuario(usuarios):
    print('''
-----------------NOVO USUÁRIO-----------------\n
Informe os dados abaixo:\n'''
)

    cpf = input("CPF (somente números): ")
    if len(usuarios) > 0:
        usuario = filtro_usuario(cpf, usuarios)
        if usuario:
            print("CPF de usuário já registrado!")
            return -1
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro-nro-bairro-cidade-sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print ("Usuário criado!\n")
    return usuarios

def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    conta = None
    while(True):
        operacao = menu()
        
        if operacao == "1":
            if conta:
                conta["saldo"], conta["extrato"] = saque(
                    saldo = conta["saldo"],
                    valor = valor,
                    extrato = conta["extrato"],
                    LIMITE_SAQUES_DIA = LIMITE_SAQUES_DIA,
                    LIMITE_SAQUE = LIMITE_SAQUE)
            else:
                print("Crie uma nova conta [4] antes de efetuar uma operação financeira.\n")
                time.sleep(2)
        
        elif operacao == "2":
            if conta:
                conta["saldo"], conta["extrato"] = deposito(conta["saldo"], valor, conta["extrato"])
            else:
                print("Crie uma nova conta [4] antes de efetuar uma operação financeira.\n")
                time.sleep(2)
        
        elif operacao == "3":
            if conta:
                extrato(conta["saldo"], extrato=conta["extrato"])
            else:
                print("Crie uma nova conta [4] antes de efetuar uma operação financeira.\n")
                time.sleep(2)
        
        elif operacao == "4":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            time.sleep(2)

            if conta:
                contas.append(conta)
        
        elif operacao == "5":
            listar_contas(contas)
            
        elif operacao == "6":
            novo_usuario(usuarios)
        
        elif operacao == "0":
            print("Encerrando o sistema...\nObrigado por utilizar o BANK System!\n")
            break
        
        else:
            print("\nNenhuma operação selecionada. Escolha uma operação válida: ")


usuarios = novo_usuario(usuarios)
while True:
    cpf = input("Informe seu CPF (somente números): ")
    if not filtro_usuario(cpf, usuarios) == None: 
        main()
        break
    else:
        print("CPF não encontrado. Tente novamente.")