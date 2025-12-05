#criação de uma class

class Veiculos:
    #atributo de classe:
    numero_rodas=4

#contrutor de objetos:
    def __init__(self,cor,modelo,preco):
        self.cor=cor
        self.modelo=modelo
        self.preco=preco

#Método de instancia
    def movimento(self):
        print(f'Sou veiculo e desloco-me numa estrada')

#Método de classe: tenho de criar um decorador antes da função para o interpretadorado saber o que fazer com ele
    @classmethod
    def get_rodas(cls):
        print(f'Todos os veiculos desta classe tem {cls.numero_rodas}')

#Método estático:
    @staticmethod
    def buzinar():
        print('BIIIP')

#criação de objetos
carro1=Veiculos('Branco','SUV',32400)
carro2=Veiculos('Preto','SEDAN',20000)

#Aceder ao metodo de instacia (chamado a partir do objeto)

carro1.movimento()
carro2.movimento()

#Aceder ao metodo de classe (chamado pela classe ou qq objeto)
Veiculos.get_rodas()#chama pela classa
carro1.get_rodas()

#aceder ao metodo estático
Veiculos.buzinar()
carro1.buzinar()

#aceder aos atributos dos objetos
print(f'A cor do carro 1 é {carro1.cor}')
print(f'A cor do carro 2 é {carro2.cor}')
print(f'Numero de rodas do carro 1 é {carro1.numero_rodas}')

#Alterar atributos
Veiculos.numero_rodas=2 #Alterar o atributo de classe
print(f'Numero de rodas do carro 1 é {carro1.numero_rodas}')
#posso alterar só apra um objeto

carro2.numero_rodas=10
print(carro1.numero_rodas)
print(carro2.numero_rodas)

