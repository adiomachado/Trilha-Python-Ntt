carros = ["gol", "celta", "palio"]

for carro in carros:
    if carro == "celta":
        print(carro)

print("*" * 80)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print("=" * 80)

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

nro_conta = 4

contas = [{'agencia': '0001', 'numero_conta': 1, 'usuario': {'nome': 'Davi Hipolito', 'data_nascimento': '10-10-2000', 'cpf': '12345678909', 'endereco': 'cic'}}, {'agencia': '0001', 'numero_conta': 2, 'usuario': {'nome': 'Adio Machado', 'data_nascimento': '20-02-1966', 'cpf': '56769490900', 'endereco': 'capao raso'}}]
print(contas[0])
print(contas[1])

conta_filtrada = [conta for conta in contas if conta['usuario']['cpf'] == "12345678909" ]

if conta_filtrada: 
    print(conta_filtrada) 
else:
    print("Não existe conta com esse número!")
