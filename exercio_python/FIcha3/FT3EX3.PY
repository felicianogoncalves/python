#EX3

nome=(input('Digite o o seu nome:'))
while len(nome) <=3:
    nome=(input('Digite um nome maior do 3 carateres:'))

idade=int(input('Digite a idade entre 0 a 100:'))
while idade <0 or idade > 100:
    idade=int(input('Por favor digite uma idade entre 0 a 100:'))

salario=float(input('O o salário:'))
while salario <0:
    salario=float(input('O salário não pode ser negativo'))

sexo=(input('Digite o seu sexo com (F) para femenino (M) para masculino: '))
while True:
    if sexo!=('F') and sexo!=('M'):
        sexo=(input('Por favor digite (F) para femenino e (M) para masculino: '))
    else:
        break

civil=input('Digite o seu esta do civel com solteiro(s),casado(c),viuvo(v),divorciado(d)' )
while civil!='s' and civil!='c' and civil!='v' and civil!='d':
        civil=(input('Entrada inválida. Por favor, digite apenas: s, c, v ou d.'))


print(f'Nome:{nome}')
print(f'Idade:{idade}')
print(f'Salário:{salario}')
print(f'Sexo:{sexo}')
print(f'Estado Civil:{civil}')