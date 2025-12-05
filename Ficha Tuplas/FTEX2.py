t1=(5,2,8,3,6,7,2,9,4,5)
t2=(1,10,3,6,7,4,1,9,8,3)
t3=(t1,t2)
print(t3)
numero=int(input('Digite um numero'))
if numero in t3[0] or numero in t3[1]:
    print(F'O numero que digitou {numero} está na T3')

print(len(t1+t2))