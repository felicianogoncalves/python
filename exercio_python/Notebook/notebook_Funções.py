def saudacao(nome):
    #print(f'Olá, {nome}')
    return 5

tipo_retorno=saudacao('Turma')
#resultado=print('6')
print('O valor de retorno é:',tipo_retorno)
print('tipo de retorno:',type(tipo_retorno))

# funçao sem retorno (com retorno NONE) e sem parametros

def exibirMensagem():
    print('Olá, bem-vindo')
# chamada  da função

exibirMensagem()#output:Olá bem-vindo

# com parametros
def saudacao(nome):
    print(f'Olá {nome},bem vindo')

# chamada  da função para argumentos 'Sara e 'Maria'
saudacao('Sara') #o output: será 'Olá Sara,bem vindo')
saudacao('Maria') #o output: será 'Olá Maria,bem vindo')

#função com 2 parametros
def fun(name,job):
    print(name,'é',job)

#chamada
fun('ze','jogador')
fun('jogador','ze')# atenção á ordem dos parametros

#passar argumentos em qualqeur ordem
fun(job='formadora',name='sara')

#Escopo
x=42 #variavel global
def fun1():
    x=0#x é variavel global
    print(x) # imprime zero que é o valor da variavel local
    return 3

fun1()# guarda 3 e imprime 0
print(x)#imprime 42
resultado=fun1()#valor da variavel é 3
print(resultado) # 3
#-----------------------------------------------------------

def verificaPar(numero):
    if numero%2 !=0:
        print('numero impar')
    else:
        print('numero par')

#chamada da função:
verificaPar(7)
verificaPar(6)

