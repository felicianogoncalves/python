palavra='Formação'
# função len()

numeroCaracteres=len(palavra)
print(numeroCaracteres)
lista=[1,4,7,3,8,0,3,4,6,7]
#numero de elementos que existe na lista
print(f'nº elementos na lista é {len(lista)}')

#elemento maior da lista em sentido numerico
print(f'numero maior da lista é {max(lista)}')

#elemento menor
print(f'menor elemento: {min(lista)}')

#somatorio do elementos da lista
print(f'somatorio: {sum(lista)}')

#exemplo de listas

lista_numeros=[1,2,3,4,5,6,7,8]
lista_frutas=['maça','pera','morango']
lista_mista=[1,'Maria',True]

Lista_vazia=[]#lista vaiza

#aceder items da lista
print(lista_frutas[0])#'maça'
#print(lista_numero[20])# erro:out of range

#imprimir a lista toda
print('lista de frutas: ',lista_frutas)
#tamanho da lista
print('Tamanho da lista numeros',len(lista_numeros))

#iterar sobre uma lista
for numero in lista_numeros:
    print('numeros da lista: ',numero)

#iterar atraves do indice

for i in range(len(lista_frutas)):
    print(f'Indice {i}:{lista_frutas[i]}')

#adicionar um fruta à lista de frutas 
lista_frutas.append('melancia')
print(lista_frutas)

#adicionar numa espicifica
lista_frutas.insert(2,'cereja')
print(lista_frutas)

#remover um elemento pelo valor
lista_frutas.remove('pera')
print('lista de frutas após remoção de pera:',lista_frutas)

#remover a partir de um indice olha para posição
lista_frutas.pop(2)
print('lista de frutas após remoção da posição 2',lista_frutas)

#Funções build-in
print('funçoes build-in')
lista=[200,3,67,378,865,12]
#maximo da lista
print('O valor maximo é',max(lista))
#minimo da lista
print('O valor minimo é',min(lista))
#ordenar lista
print('lista ordenada:',sorted(lista))

