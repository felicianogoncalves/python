# While - repete um bloco de codigo enquanto a condição for verdadeira

# while True:
    #print('loop infinito')

#imprimir todo os numeros inteiros 1 até 10

i=1

while i<=10:
    print(i)
    i=i+1
print('fim do programa')

#contagem regreciva
# n=int(input('Digite um numero maior que 0:'))

# while n>=0:
    #print(n)
    #n=n-1
# print('fim do programa')

#vamos imaginar que quero calcular e exibir a soma dos 10 primeiros numeros
#inteiros e positivos 1+2+3+4+5+6+7+8+9+10

soma=0
n=1
while n<=10:
    soma=soma+n
    print(f'Soma parcial:{soma}')
    n=n+1

#FOR
# FOR pode percorrer um sequencia (numeros, caracteres, elementos de um liste, etc.)
# ->loop controlado por contagem(range)
# -> loop de interação(percorre uma lista)

#iterar sobre um palavra -> sequencia de caracteres

palavra='Python'
print(palavra[2])
for y in palavra:
    print(y,end='')
palavra= ['red','green','blue','yellow']
print('\n',palavra[0])
for x in palavra:
    print(x,end=' ')

#o range é um função que gera uma sequencia de numeros
#exemplo1- contar de zero a 4
print('Range')
for i in range(5):
    print(i)

#exemplo2- contar de 3 a 7

for i in range(3,8):
    print(i,end=' ')

# exemplo3- contar de 10 até 30 de salto=2

for i in range(10,31,2):
    print(i,end=' ')
    if i == 24:
        break

# exemplo4- contar de traz para frente
print('contar de traz para frente')
for i in range(5,-1,-1):
    print(i,end=' ')

#Break
#interrompe o lopp imediatemente e sai dele
#mesmo que a condição se mantenha verdadeira,
#ou que ainda existam valores a percorrer
# for i in range(1,11):
#     if i  ==5:
#         break
#     print(i)
# print('fim bloco')

# #break com while
# #o utilizador vai inserir numeros para depois calcular a soma dos numeros digitados

# #o jogo para quando o ultilizar digitar numero n<=0

# soma=0
# while True:
#         numero=int(input('digite numero:'))
#         if numero <=0:
#             break
#         soma=soma+numero
# print(f'soma:{soma}')

#CONTINUE

for i in range(1,6):
    if i ==3:
        continue
    print(i)
print('fim bloco')


