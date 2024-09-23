# Sistema Bancário
import textwrap
import re
from datetime import date, datetime

def valida_cpf(cpf):
    
    formatacao = False
    quant_digitos = False
    validacao1 = False
    validacao2 = False
    cpf_ok = 0
    
    if len(cpf) > 11 :
        print("Digite somente Números")
      
    numeros = [int(digito) for digito in cpf if digito.isdigit()]
    
    #Verifica a estrutura do CPF (111.222.333-44)
    #if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
    
    formatacao = True
  
    if len(numeros) == 11:
        quant_digitos = True
  
        soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
        digito_esperado = (soma_produtos * 10 % 11) % 10
        if numeros[9] == digito_esperado:
            validacao1 = True

        soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
        digito_esperado1 = (soma_produtos1 *10 % 11) % 10
        if numeros[10] == digito_esperado1:
            validacao2 = True

        if quant_digitos == True and formatacao == True and validacao1 == True and validacao2 == True:
            #print(f"O CPF {cpf} é válido.")
            cpf_ok = 1           
        else:
            print(f"O CPF {cpf} não é válido... Tente outro CPF...")
            cpf_ok = 0
            input("Pressione Enter p/ continuar...")
    else:
        print(print(f"O CPF {cpf} não é válido... Tente outro CPF..."))
        cpf_ok = 0
        input("Pressione Enter p/ continuar...")
    return cpf_ok


data_hoje = date.today()        # pega a data do dia
mascara_data = "%d/%m/%Y %a"    # mascara para dd/mm/aaaa
data_str = (data_hoje.strftime(mascara_data)) # atribui a data_str o novo formato da data


def cadastrar_usuario(cpf, usuarios):
    usuario = pesquisar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF! ")
        input("Pressione Enter p/ continuar...")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
    input("Pressione Enter p/ continuar...")

def pesquisar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def pesquisar_conta(numero_conta, contas):
    conta_filtrada = [conta for conta in contas if conta["numero_conta"] == numero_conta]
    return conta_filtrada[0] if conta_filtrada else None
      
def cadastrar_conta(cpf, agencia, numero_conta, saldo_conta, numero_saques, usuarios):
    usuario = pesquisar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"cpf": cpf, "agencia": agencia, "numero_conta": numero_conta, "saldo_conta": saldo_conta, "numero_saques": numero_saques, "usuario": usuario}

    print("Usuário não encontrado! Favor Cadastrar antes da Conta !")
    input("Pressione Enter p/ continuar...")

def atualizar_conta(cpf, saldo_conta, numero_saques, usuarios):
    usuario = pesquisar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"cpf": cpf, "saldo_conta": saldo_conta, "numero_saques": numero_saques, "usuario": usuario}

    print("Usuário não encontrado! Favor Cadastrar antes da Conta !")
    input("Pressione Enter p/ continuar...")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          Saldo:\t{conta['saldo_conta']}
        """
        print("=" * 80)
        print(textwrap.dedent(linha))

def emitir_extrato(movimento, contas):
    # pede o cpf para imprimir somente o extrato do cpf requerido
    conta_ok = False
    cpf = int(input("Informe o CPF (somente números): "))
    cpf_ok = valida_cpf(cpf)
    if cpf_ok:
        # procura pela conta com o cpf do usuario
        conta_ok = [conta for conta in contas if conta['cpf'] == cpf ]

        if not conta_ok:
            print("Conta não encontrada com esse número!")
            return
    
        extrato = ""
        if not movimento:
            extrato = "Não houve movimentações no Período!."
        else:
            saldo_atual = 0
            for lcto, cpf in movimento.items():
                if cpf['cpf'] == cpf:
                    extrato += (f"\n{data_str} {lcto['Cpf']}:  R$ {lcto['valor']:.2f}\n")
                    saldo_atual += {lcto[valor]}
                    print(saldo_atual)

        print(extrato)
        print(f"\nSaldo:\n\tR$ {saldo_atual:.2f}")
        print("==========================================")


def main():
    
    LIMITE_SAQUES_DIARIO = 3
    AGENCIA = "0001"
   
    conta_filtrada = False
    
    extrato = ""
    chave_cpf = ""
    chave_cta = ""
    saldo = 0
    limite_saque = 500
    numero_saques = 0
    numero_deposito = 0
    nro_lcto = 0
    agencia = AGENCIA
    nro_conta = 0
    usuarios = []
    contas = []
    movimento = {}

    menu = """

    Selecione uma Opção do Menu

    (d) Depositar
    (s) Sacar
    (e) Extrato
    (u) Cadastrar Usuário
    (c) Cadastrar Conta
    (l) Listar Contas
    (f) Finalizar

    => """

    while True: # type: ignore
        
        opcao = input(menu)
        
        if opcao ==  "d":
            cpf = str(input("Informe o CPF (somente números): "))
            saldo_conta = 0.00
            cpf_ok = valida_cpf(cpf)
            
            if cpf_ok:  # se cpf foi validado 
                pesquisar_usuario(cpf, usuarios)
                # procura pela conta com o cpf do usuario
                conta_filtrada = False
                for conta in contas:
                    if conta['cpf'] == cpf:
                        conta_filtrada = True
                        print(f"conta: {conta}")
                        print(conta['saldo_conta'])
                        print(f"Conta: {conta['numero_conta']}")
                        saldo_conta = float(conta['saldo_conta'])   
                           
                if not conta_filtrada:
                    print("Conta não encontrada!")
                                
                if conta_filtrada: # se achou a conta entao pede o valor do depósito
                    
                    numero_conta = conta['numero_conta']
                    print(f"saldo: {saldo_conta}")
                    valor = float(input("Informe o Valor do Depósito: "))
                    if valor > 0 :
                        nro_lcto += 1  #numero chave extrato
                        
                        saldo_conta += valor
                        
                        #conta = cadastrar_conta(cpf, AGENCIA, numero_conta, saldo_conta,numero_saques, usuarios)
                        conta = atualizar_conta(cpf, saldo_conta, numero_saques, usuarios)
                        contas.append(conta)
                    
                        #  guarda o nro-lcto, cpf, a data e valor no dicionario de dados para poder emitir o extrato
                        movimento = {"nro_lcto": nro_lcto, "cpf": cpf, "data": data_str, "valor": valor}

                        extrato += (f"Cpf: {cpf} {data_str} Depósito: {numero_deposito} R$ {valor:.2f}\n")
                        print(f"Valor R$ {valor:.2f} Creditado com sucesso! ")
                    else: 
                        print("Valor de Depósito precisa ser maior que Zero")
                else:
                    print("Conta Inexistente!")
                   
        elif opcao == "s":  # Saque
            
            cpf = input("Informe o CPF (somente números): ")
            saldo_conta = 0.00
            cpf_ok = valida_cpf(cpf)
            
            if cpf_ok:
                 # se cpf foi validado 
                pesquisar_usuario(cpf, usuarios)
                # procura pela conta com o cpf do usuario
                conta_filtrada = False
                for conta in contas:
                    if conta['cpf'] == cpf:
                        conta_filtrada = True
                        print(f"conta: {conta}")
                        saldo_conta = float(conta['saldo_conta'])     
                        numero_conta = conta['numero_conta']
                        numero_saques = conta['numero_saques']   

                if not conta_filtrada:
                    print("Conta não encontrada!")
                                
                if conta_filtrada:
                   
                    valor = float(input("Informe o Valor do Saque: "))
                        
                    if valor > 0.00 and valor > saldo_conta:
                        print("Valor de Saldo Insuficiente!")

                    elif valor > float(limite_saque):  # maximo 500
                        print(f"Valor Limite de Saque diário (R$ {limite_saque:.2f}) Excedido!")

                    elif numero_saques >= LIMITE_SAQUES_DIARIO:
                        print(f"Número de saques diário ({LIMITE_SAQUES_DIARIO}) Excedido! Tente amanhã!") 
                                
                    else:
                        nro_lcto += 1  #incrmenta o nro de lcto do extrato
                        numero_saques += 1
                        saldo_conta -= valor
                        # Atualiza o saldo e o numero de saques na conta
                        #conta = cadastrar_conta(cpf, AGENCIA, numero_conta, saldo_conta, numero_saques, usuarios)
                        conta = atualizar_conta(cpf, saldo_conta, numero_saques, usuarios)
                        contas.append(conta)
                        
                         #  guarda o nro-lcto, cpf, a data e valor no dicionario de dados para poder emitir o extrato
                        movimento = {"nro_lcto": nro_lcto, "cpf": cpf, "data": data_str, "valor": (valor*-1)}

                        print(f"Valor do Saque: R$ {valor:.2f} Bem sucedido! ")
                else:
                    print("Conta inexistente!")

        elif opcao == "e": #Emitir Extrato
            emitir_extrato(movimento, contas)
            
        elif opcao == "u":  # Cadastrar Usuário
            
            cpf = input("Informe o CPF (somente números): ")
            cpf_ok = valida_cpf(cpf)

            if cpf_ok:
                cadastrar_usuario(cpf, usuarios)

        elif opcao == "c":  # Cadastrar Conta
            saldo_conta = 0.00
            numero_saques = 0

            cpf = input("Informe o CPF (somente números): ")
            
            cpf_ok = valida_cpf(cpf)
            if cpf_ok:
                numero_conta = len(contas) + 1
                conta_filtrada = pesquisar_conta(numero_conta, contas)
                if conta_filtrada:
                    print("Já Existe uma conta com esse cpf!")
                else:    
                    conta = cadastrar_conta(cpf, AGENCIA, numero_conta, saldo_conta, numero_saques, usuarios)

                    if conta:
                        contas.append(conta)
                        print(contas)
            else:
                print("Cpf invalido!")
                
        elif opcao == "l": # Listar as contas
            listar_contas(contas)

        elif opcao == "f":
            break
 
        #input("Pressione Enter p/ continuar...")
main()
    
