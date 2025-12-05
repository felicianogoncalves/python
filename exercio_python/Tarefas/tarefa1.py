
#Solicitação dos 3 numeros:
num1=int(input('Digite o primeiro  numero:'))
num2=int(input('Digite o segundo numero:'))
num3=int(input('Digite o terceiro numero:'))

#Colocação dos numeros em um variavel tipo lista:
numeros=[num1,num2,num3]

#Criei um variavel para buscar o primeiro numero para comparação:
menor= numeros[0]
print(menor)#só para ver o que estava a guardar

#aqui usei a variavel condição for para a variavel numero ir buscar à lista
for numero in numeros:
        if numero< menor:# aqui 'numero' vai ver se na lista tem algum numero menor que o que foi guardado na variavel 'menor' 
               menor=numero# caso a analise acima for algum momento verdade será escrito na variavel 'menor' o mesmo valor que numero
   
print(f'O menor numero é {menor}') #Irá escrever o valor que menor.
            