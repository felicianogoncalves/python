#Organizador de ficheiro
# criar um crip que:
# ----> crie uma pasta chamada documentos dentro da pasta atuaç
#-----> dentro dela, criar 3 subpastas:Texto,imagens, outros
#-----> percorrer todos os ficheiros da pasta e se :
#      for. txt mover para a pasta Textos
#      se for .jpeg ou .png mover parar imagens
#      se for qualquer outro ficheiro mover para outros

import os

import shutil # mover ficheiros
# 1 criar a pasta documentos e subpastas

base=r'C:\Users\cesae\Desktop\Documentos'
subspastas=['Textos','Imagens','Outros']

for sub in subspastas:
    os.makedirs(os.path.join(base,sub),exist_ok=True)
print('Pastas criadas com sucesso')

#Quero percorrer os ficheiro da pasta atual


ficheiros=os.listdir(base)
print(ficheiros)

for ficheiro in ficheiros:
    caminho_completo = os.path.join(base, ficheiro)
    #temos que filtrar as pastas
    if os.path.isfile(caminho_completo): # verifica se é um ficheiro neste 'caminho_completo'
        # extrair os ficheiros
        nome,ext=os.path.splitext(ficheiro)
        # decidir para onde mover
        if ext == '.txt':
            destino=os.path.join(base,'textos',ficheiro)
        elif ext =='.jpg' or ext=='.png':
            destino=os.path.join(base,'Imagens',ficheiro)
        else:
            destino=os.path.join(base,'Outros',ficheiro)
        # mover o ficheiro
        shutil.move(caminho_completo,destino)
        print(f'Movido:{ficheiro} para a pasta {destino}')