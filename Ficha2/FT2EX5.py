#EX5

print('***********GRANDEZAS ELETRICAS***********')
print('1. Tensão (em Volts)')
print('2. Resistencia (em Ohm)')
print('3. Corrente (em Amperes)')
print('*****************************************')

opcao=int(input('Qual a grandeza que deseja calcula?'))

if opcao==1:
    corrente=float(input('Digita a corrente:'))
    ressistencia=float(input('Digite a Ressistencia:'))
    tensao=corrente*ressistencia
    print(f'A valor tensão é {tensao} volts')
elif opcao==2:
    corrente=float(input('Digita a corrente:'))
    tensao=float(input('Digite a Tensão:'))
    ressistencia=tensao/corrente
    print(f'A valor tensão é {ressistencia} Ohm')
elif opcao==3:
    ressistencia=float(input('Digita a Ressistencia:'))
    tensao=float(input('Digite a Tensão:'))
    corrente=tensao/ressistencia
    print(f'A valor tensão é {corrente} Amperes')
else:
    print('A opção que selecionou é invalida!')




