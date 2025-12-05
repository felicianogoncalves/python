t=('segunda','terça','quarta','quinta','sexta','sabado','domingo')

numero=int(input('Digite um numero de 1 a 7:'))

if 1<numero<7 :
    print(f'O dia será selecionado é {t[numero -1]}')