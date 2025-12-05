
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

#Classe derivada
class Carro(Veiculos):
    #metodo construtor
    def __init__(self, cor, modelo, preco,marca):
        super().__init__(cor, modelo, preco)
        self.marca=marca

    #sobreeescrever o metodo da classe mae
    def movimento(self):
        print(f'Sou um veiculo da marca {self.marca} e desloco-me numa estrada')

#Novo metodo exclusivo da classe filha
    def car_info(self):
        print(f'{self.marca},{self.cor},{self.modelo},{self.preco}')


carro1=Carro('branco','SUV',30000,'BMW')
carro1.movimento()
carro1.buzinar()
print(carro1.numero_rodas)
veiculo1=Veiculos('branco','SUV',30000)
veiculo1.movimento()
carro1.movimento()
carro1.car_info()
#veiculo.car_infor() isto não é possivel porque veiculo é da classe Pai(Veiculos)
