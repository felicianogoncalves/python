import os

# Diretorio atual
diretorio_atual=os.getcwd()
print(f'directorio atual',diretorio_atual)

#listar ficheiro e pastas
items=os.listdir(diretorio_atual)
print(f'Items do diretorio', items)

#criar novos ficheiros
#temos de verificar sempre se existem ficheiros com aquele nome
#criar no diretorio atual

if not os.path.exists('pasta_batatinhas'):
    os.mkdir('pasta_batatinhas')

#criar a pasta noutro diretorio

caminho=r"C:\Users\cesae\Desktop\pastalaranjas" #o "r" permite ignorar os \ e olhar como um conteudo cru
if not os.path.exists(caminho):
    os.makedirs(caminho)
else:
    print('A pasta já existe')

caminho2=r"C:\Users\cesae\Desktop"
if not os.path.exists(caminho2):
    pasta1= os.path.join(caminho2,'pastalaranjas')
    os.mkdir(pasta1)
else:
    print('A pasta ja existe')

#criar pasta aninhadas

if not os.path.exists(caminho):
    pasta2=os.path.join(caminho,'pastamaça')
    os.makedirs(pasta2)
else:
    print('A pasta ja existe')

#criar ficheiro dentro da pasta_batatinhas

caminho_ficheiro=os.path.join(caminho,'caminhos_txt')
with open(caminho_ficheiro,'w') as file:
    pass # criar um ficheiro vazio
    file.write('primeira linha do ficheiro')

#renomear ficheiros
novo_caminho=os.path.join(caminho,"ruas.txt")
os.rename(caminho_ficheiro,novo_caminho)

#Apagar ficheiro

os.remove(novo_caminho) #apaga ficheiro rua.txt

#Apagar pasta
os.rmdir(pasta2)