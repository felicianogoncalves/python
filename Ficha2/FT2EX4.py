#EX4

camisas=int(input('Insira o numero de camisas:'))
preco=17.5

if camisas<=5:
    valor=(preco*0.97)*camisas
    print(f'O valor a pagar é {valor:.2f}€')
elif camisas<10:
    valor=(preco*0.95)*camisas
    print(f'O valor a pagar é {valor:.2f}€')
else:
    valor=(preco*0.93)*camisas
    print(f'O valor a pagar é {valor:.2f}€')
