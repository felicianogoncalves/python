#EX4      

a=int(80000)
b=int(200000)
anos=0

while a<=b:
    a=int(a*1.03)
    anos=anos+1
    b=int(b*1.015)

print(f'Ao fim de {anos} anos o Pais A ficou com {a} habitantes e o Pai B ficou com {b} ')