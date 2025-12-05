import json
#transforma o ficheiro json em um dicionario

with open('dados_json.json','r',encoding="utf-8") as file:
    dados=json.load(file)
    print(dados)
    print(type(dados))
    
print(dados["nome"])
print(dados["idade"])
print(dados["cidade"])

#modificar dados
#criaçaõ de uma nova chave-valor no jason

dados["profissão"]="eng"

print(dados)

# para guardar no ficheiro as alterações
with open("dados_json.json", 'w',encoding='utf-8') as file:
    json.dump(dados,file,ensure_ascii=False,indent=4)


# ficheiro jason dados1_json.json

with open("dados1_json.json",'r', encoding='utf-8') as file:
    modulos=json.load(file)

print(modulos)

#aceder a elementos
print(modulos[1])
#adicionar um elemento
modulos.append('JavaScript')

print(modulos)

with open("dados1_json.json", 'w',encoding='utf-8') as file:
    json.dump(modulos,file,ensure_ascii=False,indent=4)

    ###### FIcheiro JSON dados2_json.json

#empresa --> chave com valor string
#Funcionario --> chave com valor array/lista de objetos(dicionarios)
#Cada funcionario é um dicionario com nome e idade

with open("dados2_json.json", 'r',encoding='utf-8') as file:
    dados_json=json.load(file)
    print(dados_json)

#aceder dados:
#empresa
print("Empresa:",dados_json["empresa"])

#Funcionarios (lista de dicionarios)
funcionarios=dados_json["funcionarios"]

print(funcionarios)
#Aceder elementos dentro do array/(lista)
for fun in funcionarios:
    print(f'{fun['nome']} - {fun['idade']}')

#alterar dados
#Alterar a idade da Ana

funcionarios[0]["idade"]=31

print(funcionarios)

#adicionar um novo funcionario

funcionarios.append({"nome":"Maria","idade":40})

print(funcionarios)

#Escrever no ficheiro com dados atualializados
with open("dados2_json.json", 'w',encoding='utf-8') as file:
    json.dump(dados_json,file,indent=4,ensure_ascii=False)
    print(dados_json)