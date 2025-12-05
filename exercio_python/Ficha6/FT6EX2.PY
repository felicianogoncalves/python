a=10
b=20

def calculadora():
    operador=input('Digite o operador(+,-,/,*):')
    if operador=='+':
        soma=a+b
        print(soma)
    elif operador=='-':
        subtracao=a-b
        print(subtracao)
    elif operador == '*':
        multiplicação=a*b
        print(multiplicação)
    elif operador== '/':
        divisao=a/b
        print(divisao)
    else:
        print('Operador nao suportado')

calculadora()

