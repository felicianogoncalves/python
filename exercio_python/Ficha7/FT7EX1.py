class Cliente:
    #atributo classe
    empresa='Tech Solutions'
    #Metodo contrustor:
    def __init__(self,nome,email,telefone):
        self.nome=nome
        self.email=email
        self.telefone=telefone
    #Metodo de instancia:

    def apresentar(self):
        print(f'Olá eu sou o {self.nome} e o email é {self.email}')
#Método de classe: tenho de criar um decorador antes da função para o interpretadorado saber o que fazer com ele
    @classmethod
    def get_empresa(cls):
        print(f'Todos os cliente pertencem à empresa {cls.empresa}')

#Método estático:
    @staticmethod
    def saudacao():
        print('Bem vindo ao sistema de cliente!')

cliente1=Cliente('José','jose@hotmail.com',913333333)
cliente2=Cliente('Maria','Maria@hotmail.com',913333334)
cliente3=Cliente('Antonio','Antonio@hotmail.com',913333335)

cliente1.apresentar()
cliente2.apresentar()
cliente3.apresentar()

cliente1.get_empresa()

cliente1.saudacao()

print(f'O nome do cliente 1 é {cliente1.nome}')
print(f'O nome do cliente 3 é {cliente3.telefone}')
print(f'O nome do cliente 2 é {cliente2.email}')

#Alterar o email de um dos clientes e imprimir o novo valor no ecrã

print(f'O email do cliente 1 é {cliente1.email}')
cliente1.email='jose90@hotmail.com'
print(f'O email do cliente 1 é {cliente1.email}')


