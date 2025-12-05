from FT7EX2 import Livro

class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano,numero_paginas):
        super().__init__(titulo, autor, ano)
        self.numero_paginas=numero_paginas

    def apresentar(self):
        print(f' O numero de paginas do {self.titulo} é de {self.numero_paginas}')

fisico1=LivroFisico('Carochinha','zé',2000,1000)
fisico2=LivroFisico('O Benfica','Eusebio',1900,2000)
fisico3=LivroFisico('Portugal','Camoes',1750,250)

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano,formato):
        super().__init__(titulo, autor, ano)
        self.formato=formato
    
    def apresentar(self):
        print(f'O Livro digital {self.titulo} está no formato {self.formato} ')

digital1=LivroDigital('real madrid','Di stefano',2010,'pdf')
digital2=LivroDigital('Biblia','Deus',0,'excel')
digital3=LivroDigital('Mundo','python',100,'pdf')

fisico1.apresentar()
fisico2.apresentar()
fisico3.apresentar()
digital1.apresentar()
digital2.apresentar()
digital3.apresentar()

fisico1.boas_vindas()
fisico1.get_categoria()

print(f'O livro {fisico1.titulo} tem como autor {fisico1.autor} do ano {fisico1.ano} e tem {fisico1.numero_paginas} paginas')
print(f'O livro {digital1.titulo} tem como autor {digital1.autor} do ano {digital1.ano} e está no formato {digital1.formato}')