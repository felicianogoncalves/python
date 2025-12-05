lista=list(range(1,101))
print(f'a) soma ={sum(lista)}')

somamult_3=sum(x for x in lista if x % 3==0)

print('soma dos Multiplos de 3')

impar=[]
par=[]
for i in range(len(lista)):
    if lista[i] % 2 !=0:
        impar.append(lista[i])

print(f'Impar {impar}')

for i in range(len(lista)):
    if lista[i] % 2 ==0:
        par.append(lista[i])

print(f'Par {par}')

div_10=[]

for num in lista:
    if num % 10 ==0:
        div_10.append(num)

print(f'Os divisores de 10 são:',div_10)
        

