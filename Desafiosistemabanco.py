# Sistema Bancário
from datetime import date, datetime

data_hoje = date.today()        # pega a data do dia
mascara_data = "%d/%m/%Y %a"    # mascara para dd/mm/aaaa
data_str = (data_hoje.strftime(mascara_data)) # atribui a data_str o novo formato da data

extrato = ""
saldo = 0
limite_saque = 500
numero_saques = 0
numero_deposito = 0
LIMITE_SAQUES_DIARIO = 3

menu = """

Selecione uma Opção do Menu

(d) Depositar
(s) Sacar
(e) Extrato
(f) Finalizar

=> """

while True: # type: ignore
    
    opcao = input(menu)
    
    if opcao ==  "d":
    
        valor = float(input("Informe o Valor do Depósito: "))
       
        if valor > 0 :
            numero_deposito += 1
                
            saldo += valor

            #  guarda a data, numero do deposito e valor
            extrato += (f"{data_str} Depósito: {numero_deposito} R$ {valor:.2f}\n")
            print(f"Valor R$ {valor:.2f} Creditado com sucesso! ")

        else:
            print("Valor de Depósito precisa ser maior que Zero")
    
    elif opcao == "s":
       
        mensagem = ("Informe o Valor do Saque: ") 
        
        valor = float(input(mensagem))
       
        if valor > 0.00:
            
            if valor > saldo:
                print("Valor de Saldo Insuficiente!")

            elif valor > float(limite_saque):  # maximo 500
                print(f"Valor Limite de Saque diário (R$ {limite_saque:.2f}) Excedido!")

            elif numero_saques >= LIMITE_SAQUES_DIARIO:
                print(f"Número de saques diário ({LIMITE_SAQUES_DIARIO}) Excedido! Tente amanhã!") 
            
            else:
                
                numero_saques += 1
                saldo -= valor
                extrato += (f"{data_str} Saque   : {numero_saques} R$ {valor:.2f}\n")
                   
                print(f"Valor do Saque: R$ {valor:.2f} Bem sucedido! ")
                
        else:
            print("Operação Invalida!")
       
    elif opcao == "e":

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "f":
        break

    else:
        print("Selecione uma opçao válida!")

    input("Pressione Enter p/ continuar...")

    
