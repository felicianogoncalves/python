frutas= {
    'maça':10,
    'banana':5
    }

valor=input('Digite qual fruta quer saber quantidade:')


if valor in frutas:
    print(f'A quantidade de {valor} é {frutas[valor]}')
else:
    print('Esse nome nao consta na lista')