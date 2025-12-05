class Livro:
    categoria='Literatura'

    def __init__(self,titulo,autor,ano):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano

    def  descricao(self):
        print(f'O titulo do livro é {self.titulo} o autor é {self.autor} e o ano é {self.ano}')

    @classmethod
    def get_categoria(cls):
        print(f'A categoria é {cls.categoria}')

    @staticmethod
    def boas_vindas():
        print(f'Bem vindo à Biblioteca Virtual!')

livro1=Livro('Cozinha','ze',1990)
livro2=Livro('AWS','Rick',2005)
livro3=Livro('Azure','John',2010)

livro1.descricao()
livro2.descricao()
livro3.descricao()
livro1.get_categoria()
livro1.boas_vindas()

print(f'O autor do livro 1 tem o autor {livro1.autor} o Titulo é {livro1.titulo} e o ano de criação é {livro1.ano}')
print(f'O autor do livro 2 tem o autor {livro2.autor} o Titulo é {livro2.titulo} e o ano de criação é {livro2.ano}')
print(f'O autor do livro 3 tem o autor {livro3.autor} o Titulo é {livro3.titulo} e o ano de criação é {livro3.ano}')

livro3.titulo='Azure 2.0'

print(f'O novo Titulo do livro 3 é {livro3.titulo}')