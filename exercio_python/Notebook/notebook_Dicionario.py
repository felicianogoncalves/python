#cria um dicionario

aluno={
    'nome':'Maria',
    'idade':22,
    'curso':'AWS',
}

codigo={
    10:'azul',
    2:'amarelo',
    31:'azul'
}

print(aluno)#imprime todo o dicionario

#para aceder a valores especificos
print(aluno['curso'])

#alterar e adicionar valor
aluno['idade']=45 # altera o valor da chave idade 22->45
print(aluno)

aluno['morada']='Braga'#adicionar um novo key-value('morada':'Braga')
print(aluno)

#remover pela chave 
aluno.pop('curso')# remove a chave e valor associado
# del aluno['curso']

#Iterar spnre dicionarios:

for chave in aluno:
    print(chave,aluno[chave])

#dicionario de produtos com preços

produtos={
    'arroz':1.99,
    'feijão':2.45,
    'leite':0.89
}

total=0
for preco in produtos.values():
    total=total+preco
print('total:',total)

for chave in produtos.keys():
    print (' Chave',chave)

for chave,preco in produtos.items():
    print(f'{chave} e {preco}')
