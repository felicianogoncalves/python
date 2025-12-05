#Solicitação dos 3 numeros:
num1=int(input('Digite o primeiro  numero:'))
num2=int(input('Digite o segundo numero:'))
num3=int(input('Digite o terceiro numero:'))


#metodo para verificar o numero 1 se é o menor ou maior
if num1<num2 and num1<num3:# se isto for verdade escreve o numero1 na variavel menor senão avança
    menor=num1
elif num1>num2 and num1>num3:  # se isto for verdade escreve o numero1 na variavel maior senão avança
    maior=num1
else:
    segundo=num1 # se chegou até aqui está tudo descado é porque é o numero do meio

#metodo para verificar o numero 2 se é o menor ou maior
if num2<num1 and num2<num3:# se isto for verdade escreve o numero2 na variavel menor senão avança
    menor=num2
elif num2>num1 and num2>num3:# se isto for verdade escreve o numero2 na variavel maior senão avança
    maior=num2
else:
    segundo=num2 # se chegou até aqui está tudo descado é porque é o numero do meio

#metodo para verificar o numero 3 se é o menor ou maior
if num3<num2 and num3<num1:# se isto for verdade escreve o numero3 na variavel menor senão avança
    menor=num3
elif num3>num2 and num3>num1:# se isto for verdade escreve o numero3 na variavel maior senão avança
    maior=num3
else:
    segundo=num3# se chegou até aqui está tudo descado é porque é o numero do meio

print(f'os numeros de ordem crescente {menor},{segundo},{maior}') # irá escrever o conforme a ordem solicitada

#pensei usar o 'for in range' mas não estava a conseguir por isso fiz assim e deu!

