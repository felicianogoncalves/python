print('===Conversor de Moedas===')
print('1 - Converter para Dolar (taxa 1.12)')
print('2 - Converter para Libra (taxa 0.85)')
print('3 - Definir nova moeda')
opcao=int(input('Escolha uma opção(1/2/3):'))
taxadolar=1.12
taxalibra=0.85

if opcao == 1:
    def dolar():
        valor1=float(input('Digite a quantidade para converter:'))
        valordolar=valor1*taxadolar
        print(f'O valor convertido para Dolar é {valordolar:.2f}$')
        return valordolar
    dolar()
elif opcao == 2:
     def libra():
        valor2=float(input('Digite a quantidade para converter:'))
        valorlibra=valor2*taxalibra
        print(f'O valor convertido para Libra é {valorlibra:.2f}£')
        return valorlibra
     libra()
elif opcao == 3:
    def nova():
        nome=(input('Digite o nome da moeda:'))
        taxadif=float(input('Digite a taxa:'))
        valor3=float(input('Digite a quantidade para converter:'))
        valordif=valor3*taxadif
        print(f'O valor convertido para {nome} é {valordif:.2f}')
    nova()
else:
    print(f'O valor que digitou não está nas opções')
        

