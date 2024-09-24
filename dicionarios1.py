contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    
    if ("3344" in valor['telefone']):
        print(valor)  #printa o nome e telefone
        
    else:
        print(valor['telefone']) # printa somente o telefone
    
   
    #print(chave, valor)
contatos.clear() # limpa o dicionario
print(contatos)  # printa só {}
# update atualiza o dicionário com novos dados
contatos.update({"gio@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos)  

# values
resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)