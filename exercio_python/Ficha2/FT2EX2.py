#EX2

idade=(int(input('Digite a idade do atleta:')))

if idade>=18:
    print('O altleta é Sénior')
elif idade>=14:
    print('O altleta é Júnior')
elif idade>=11:
    print('O altleta é Juvenil')
elif idade>=8:
    print('O altleta é Iniciado')
elif idade>=5:
    print('O altleta é Infantil')
else:
    print('O valor é baixo deverá colocar idade acima de 5 para se enquadrar nas categorias')


