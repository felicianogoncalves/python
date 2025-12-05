# este ficheiro main.py vai utilizar as funçoes do ficheiro bibliotecadefuncoes.py
#import Biblioteca_funções as bf
#dar um nome do ficheiro para ser mais facil usar, porque para aceder ás funções tenho de chama o modulo
#resultado=bf.somar(3,5)

from Biblioteca_funções import * 
#importa tudo do ficheiro e só tenho que usar o nome das funções

#chamada ao metodo soma

resultado=somar(3,5)
resultado2=subtrair(6,5)
resultado3=multiplicar(3,5)

print(resultado)
print(resultado2)
print(resultado3)