
from FT7EX1 import Cliente

class ClientePremium(Cliente):
    def __init__(self,nome,email,telefone,percentagem):
        super().__init__(nome,email,telefone)
        self.percentagem=percentagem

    def apresentar(self):
        print(f'O ClientePremium {self.nome} tem o desconto de {self.percentagem}%')

premium1=ClientePremium('José','jose@email.com',912345678,10)
premium2=ClientePremium('André','andre@email.com',912345675,15)
premium3=ClientePremium('Rui','rui@email.com',912345679,20)

class ClienteRegular(Cliente):
    def __init__(self, nome, email, telefone):
        super().__init__(nome, email, telefone)

    def apresentar(self):
        print(f'Cliente {self.nome} Regular')

regular1=ClienteRegular('Maria','maria@email.com',912345674)
regular2=ClienteRegular('Renato','Renato@email.com',912345673)
regular3=ClienteRegular('Ana','ana@email.com',912345672)


premium1.apresentar()
premium2.apresentar()
premium3.apresentar()
regular1.apresentar()
regular2.apresentar()
regular3.apresentar()

premium1.saudacao()
premium1.get_empresa()

print(f'O cliente {premium1.nome} é um cliente premium e tem desconto de {premium1.percentagem}%')
print(f'O cliente {regular1.nome} é um cliente regular e não tem desconto,mas o seu email é {regular1.email}')