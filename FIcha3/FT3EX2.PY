#EX2

nome=str(input('Digite o seu nome:'))
senha=input('Digite a senha:')

while senha==nome:
    print('Por favor nao digite a senha igual ao nome')
    senha=input('Digite a senha novamente')

