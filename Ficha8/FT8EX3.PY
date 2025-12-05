
with open('dados_pessoais.csv','r',encoding='utf-8') as file:
    conteudo=file.readlines()
    print(conteudo)
    for linha in conteudo[1:]:
        partes=linha.strip().split(';')
        print(partes[0])

idades=[]
for linha in conteudo[1:]:
    partes=linha.strip().split(';')
    idades.append(int(partes[2]))

print(idades)

media=sum(idades)/len(idades)
print(f'A média de idades é:{media} anos')
    
with open('dados_pessoais.csv','a',encoding='utf-8') as file:
    nome=input('Digite o nome:')
    morada=input('Digite a morada:')
    idade=int(input('Digite a idade:'))
    file.write(f'{nome};{morada};{idade}\n')
    
with open('dados_pessoais.csv','r',encoding='utf-8') as file:
    conteudo=file.readlines()
    print(conteudo)
    for linha in conteudo[1:]:
        partes=linha.strip().split(';')
        print(partes)


