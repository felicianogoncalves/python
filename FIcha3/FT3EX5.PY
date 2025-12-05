#EX5       

a=int(input('Digite o numero de habitantes A:'))
while a<0:
    a=int(input('Digite o numero de habitantes A superior a 0:'))
b=int(input('Digite o numero de habitantes B:'))
while b<0:
    b=int(input('Digite o numero de habitantes B superior a 0:'))
anos=0
taxaa=float(input('Digite a taxa anual do pais A em percentagem'))
while taxaa<0:
    taxaa=float(input('Digite a taxa anual do pais A em percentagem numero maior que 0'))
taxaa=(taxaa/100)+1
taxab=float(input('Digite a taxa anual do pais B em percentagem'))
while taxab<0:
    taxab=float(input('Digite a taxa anual do pais B em percentagem numero maior que 0'))
taxab=(taxab/100)+1

while a<=b:
    a=(a*taxaa)
    anos=anos+1
    b=(b*taxab)

a=int(a)
b=int(b)

print(f'Ao fim de {anos} anos o Pais A ficou com {a} habitantes e o Pai B ficou com {b} ')