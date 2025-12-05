#Ex1
print("10+20x30=",10+20*30)
print("4^2/30=",(4**2)/30)
print("(94+2)x6-1=",(94+2)*6-1)

#Ex2
a=3
b=5
print("O resultado de 2a x 3b =",2*a*3*b)

#Ex3
 #Ex3 idade=int(input("Digite a sua idade:"))
 #Ex3 altura=float(input("Digite a sua altura em metros:"))
 #Ex3 maior_idade=idade>=18
 #Ex3 if maior_idade == 1:
    #Ex3 status_idade="maior de idade"
 #Ex3 else:
    #Ex3 status_idade="menor de idade"
 #Ex3 nome=str(input("Digite o seu nome completo:"))
 #Ex3 localidade=str(input("Digita a sua localidade:"))

#Ex3 print(f"A sua idade é {idade} e é do tipo",type(idade))
#Ex3 print(f"Voce é {status_idade} e é do tipo ",type(maior_idade))
#Ex3 print(f"A sua altura é {altura} e é do tipo",type(altura))
#Ex3 print(f"O seu nome completo é {nome} e é do tipo",type(nome))
#Ex3 print(f"A sua  localidade é {localidade} e é do tipo",type(localidade))


#Ex4
print("EX4")
a=4
b=10
c=5.0
d=1
f=5

print(f"a é igual c?:{a==c}") #false
print(f"a é menor que b?:{a<b}")#True
print(f"d é maior b?:{d>b}")#False
print(f"c é diferente f?:{c!=f}")#false
print(f"a é igual que b?:{a==b}")#false
print(f"c é menor que a?:{c<a}")#false
print(f"b é maior que a?:{b>a}")#true
print(f"c é maior ou igual que f?:{c>=f}")#True
print(f"f é maior ou igual que c?:{f>=c}")#True
print(f"c é menor ou igual que f?:{c<=f}")#True

#Ex5
print("EX5")
caso1=((1>2) and 1)or 0
caso2=((10>3)and 0)or 0
caso3=((5>1)and 1)or 1

print("O valor do caso 1 é:",caso1)
print("O valor do caso 2 é:",caso2)
print("O valor do caso 3 é:",caso3)

#Ex6

 #Ex6 tot_eleitores=(int(input("digite o numero total de eleitores do municipio:")))
 #Ex6 brancos=(int(input("digite o numero de votos em branco:")))
 #Ex6 nulos=(int(input("digite o numero de votos nulos:")))
 #Ex6 votos_validos=tot_eleitores-(brancos+nulos)
 #Ex6 pbrancos=(brancos/tot_eleitores)*100
 #Ex6 pnulos=(nulos/tot_eleitores)*100
 #Ex6 pvoto_valido=(votos_validos/tot_eleitores)*100

 #Ex6 print(f"A percentagem dos votos em branco é {pbrancos}%")
 #Ex6 print(f"A percentagem dos voto nulos é {pnulos}%")
 #Ex6 print(f"A percentagem dos votos validos é {pvoto_valido}%")

#Ex7
#Ex7 idade=(int(input("digite a sua idade:")))
#Ex7 meses=(int(input("Digite o numero do mes do seu aniversário:")))
#Ex7 dia=(int(input("Digite o dia do seu aniversario:")))

#Ex7 idade_dias=idade*365
#Ex7 meses_dias=meses*30
#Ex7 total_dias=idade_dias+meses_dias+dia

#Ex7 print(f"A sua idade me dias é de {total_dias}")

#Ex8

#Ex8 num1=int(input("Digite o primeiro numero maior que 0:"))
#Ex8 while num1<= 0:
    #Ex8 num1=int(input("Número inválido.Digite um numero maior que 0:"))

#Ex8 num2=int(input("Digite o segundo numero maior que 0:"))
#Ex8 while num2<= 0:
    #Ex8 num2=int(input("Número inválido.Digite um numero maior que 0:"))

#Ex8 print(f"Soma {num1}+{num2}={num1+num2} ")
#Ex8 print(f"Subtração {num1}-{num2}={num1-num2} ")
#Ex8 print(f"Multiplicação {num1}x{num2}={num1*num2} ")
#Ex8 print(f"Divisão {num1}:{num2}={num1/num2} ")
#Ex8 print(f"Exponenciação {num1}^{num2}={num1**num2} ")
#Ex8 print(f"Resto da divisão {num1}%{num2}={num1%num2} ")

#Ex9 
#Ex9 nomed1=input("Digite o nome da disciplina:")
#Ex9 notad1=float(input('Coloque o valor da  primeira nota:'))
#Ex9 nomed2=input("Digite o nome da disciplina:")
#Ex9 notad2=float(input('Coloque o valor da  nota:'))
#Ex9 print(f'A média das notas é {(notad1+notad2)/2:.1f}%')

#Ex10

#Ex10 valor=float(input('Digite o valor em metros:'))
#Ex10 calcentrimentro=valor*100
#Ex10 print(f'Os metros {valor}m em centrimetro é {calcentrimentro}cm')

#Ex11
#Ex11 from math import pi 

#Ex11 raio=float(input('digite o raio do circulo'))
#Ex11 p=2*pi*raio
#Ex11 area=pi*raio**2
#Ex11 print(f'O perímetro desse circulo é {p:.2f} e a sua área é {area:.2f}')

#EX12
#EX12 import math 

#EX12 graus=float(input('Digite o angulo'))

#EX12 radians=math.radians(graus)

#EX12 seno=math.sin(radians)
#EX12 coseno=math.cos(radians)
#EX12 tangente=math.tan(radians)

#EX12 print(f'O angulo {graus} em radiano fica {radians:.3f} e o seu senno é {seno:.3f}, o coseno{coseno:.3f} e a sua tangente é {tangente:.3f}')








