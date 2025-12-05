print("Olá Python")
nome="Júnior"
if nome == "Júnior":
    print("Acertou")

a=10
print("endereço:",id(a))

# alterar a variável a
a=a+5
print("endereço:",id(a))

# Para variaveis constante usar sempre em letrar maiusculas

#Tipos de Variaveis -- type
print("*********TIPOS DE VARIAVEIS********")
nome="python" # Isto é um string str
horas_aulas=50 # Isto é um int
preco=150.50 # Isto é um float(tem parte decimal)
activo=True #Isto é um Bool
desativo=False # Isto é Bool
print("O valor da variavel horas_aulas é:",type(horas_aulas))
print("O valor da variavel nome é:",type(nome))
print("O valor da variavel preço é:",type(preco))
print("O valor da variavel activo é:",type(activo))

#Lista
lista=[1,2,3,4]
print("O valor da variavel lista é:",type(lista))

#Tipo: None (ausencia de valor)
vazio=None
print("O valor da variavel vazio é:",type(vazio))
#None é um objeto que representa "nenhum Valor" ou vazio
# None não é zero nem uma string vazia, nem False
print(vazio==0) #False
print(vazio==False) #False
print(vazio=="") #False

# bool (True or False) pode ser entendido como int (1 or 0)
print(False+2)# 0+2=2
print(True+3)# 1+3=4

#Strings
print("*******STRINGS********")
palavra="ola   "
print("Tamanho da  variavel palavra",len(palavra),"caracteres")
print("Qual é o caractere que está na posição 0? Caractere da posição 0 é ",palavra[0])
print("Qual é o caractere que está na posição 1? Caractere da posição 1 é ",palavra[1])
print("Qual é o caractere que está na posição 2? Caractere da posição 2 é ",palavra[2])
palavra_maiusculas=palavra.upper()
print("Palavra em maiscular",palavra_maiusculas)
#Conctenar string
print("Conctenar string")
s=" ola"
s=s+" Mundo"
print(s)
m=s*3
print(m)

#Formatação de Strings
print("FORMATAÇÃO DE STRINGS")
#concatenação -> operador"+"
nome="Júnior"
apelido="Gonçalves"
print("Olá "+nome+" "+apelido+".")
print("Olá",nome,apelido)

#metodo format
print("metodo format")

nome="Júnior"
idade=30
print("Olá O {0} tem {1} anos {1} {0}".format(nome,idade))
print("Olá O {n} tem {i} anos {i} {n}".format(n=nome,i=idade))

# interpolação(f-strings) só dá para python superior 3.6
print("Interpolação f-strings")
nome="Júnior"
idade=30
altura=1.8012
print(f"Olá o {nome}, tem {idade} anos e tem de altura {altura:.2f}m")
# casas decimais :.2f

#Conversão implicita
print("Conversão implicita")
num1=3
num2=10.567
resultado=num1+num2
print(f"Resultado= {resultado}, tipo do resultado {type(resultado)}")

#Conversão explicita
print("Conversão explicita")
num=int("123") # converter um string em um numero inteiro
print("Tipo de num:",type(num))
preco=float("12.40")
print("Tipo de preço:",type(preco))
preco=preco+0.50
print(preco)

#Input
print("*****INPUT*****")
 #idade= int(input("Digite a sua idade:"))
 #peso= float(input("Digite o seu peso:"))
 #print(f"A sua idade é {idade} anos e o seu peso é {peso} Kg")

 #Operador Matematicos
 #Criar um programa que peça numeros e em seguida mostra a soma, subtração,divisão,multiplicação,exponenciação

 #num1=float(input("Introduza numero 1:"))
 #num2=float(input("Introduza numero 2:"))
print("Soma: ",num1+num2)
print("Subtração: ",num1-num2)
print("Multiplicação: ",num1*num2)
print("Divisão: ",num1/num2)
print("Exponência: ",num1**num2)

#Contadores
a=2
a=a+1
a+=1

#operadores logicos
a=4
b=6
print(f"a é igual a b?:{a==b}") #False
print(f"a>b=:{a>b}")#False
print(f"a é diferente de b?:{a!=b}")

#Exemplo combinado
print(f"a>b e a>0: {(a>b)and(a>0)}")

#Importação de Bibliotecas Internas

#quero calcular a raiz quadrada de 5
print(f"raiz quadrada:{5**(1/2)}") # matematicamente

#ou posso mais simples importar o modula math

import math

print("Raiz quadrada de 5 é :",math.sqrt(5))
print("PI:",math.pi)


#SÓ UMA PARTE DO MODULO

from math import sqrt,pi

print(sqrt(2))


#************************CONDICIONAIS****************************

# nota1=float(int(input'Digite o valor da nota 1:'))
# nota2=float(int(input'Digite o valor da nota 2:'))

# cálculo da média
# media=(nota1+nota2/2)

#if simples

# if media>=10:
    #print("Aprovado")

# if media<10:
    #print("Reprovado")
# print('Acabou o programa')

# if e else

#if media>=10:
    #print('Aprovado')
# else:
    #print('reprovado')

# if elif else

#if media>=10:
    #print('Aprovado')
# elif media>=18
    #print('Excelente')
# else:
    #print('reprovado'

