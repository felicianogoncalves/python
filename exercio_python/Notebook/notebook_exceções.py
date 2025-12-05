num1=1
num2='as'

#querer dividir o num1/num2 e apanhar alguma excecao(erro)

def dividir(num1,num2):
    try:
        return num1/num2
    except Exception as e:#exceção genérica
        print('ERRO:',e)

print(dividir(num1,num2))

print('continuação do meu codigo')


#
print('************************')
def soma(a,b):
    resultado2=a+b
    return resultado2
soma_numeros=soma(2,3)
print(soma_numeros)