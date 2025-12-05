modulos=[
    'introdução á programação\n',
    'programa em python\n',
    'hardware e redes\n',
    'fundamentos de bases de bases\n'
]

with open('moduloAWS.txt','w',encoding='utf=8') as ficheiro:
    ficheiro.writelines(modulos)
    print('Ficheiro com conteudo criado com sucesso')



with open('moduloAWS.txt','r',encoding='utf-8') as ficheiro:
    conteudo=ficheiro.read()

print('Conteudo do ficheiro:')
print(conteudo)

with open('moduloAWS.txt','r',encoding='utf-8') as ficheiro:

    linhas=ficheiro.readlines()
print(linhas)
print('lista:',linhas)
print('2º linha:',linhas[1].strip())