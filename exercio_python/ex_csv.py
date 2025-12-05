#abrir para ler o conteudo

with open('dados_csv.csv','r',encoding='utf-8') as file:
    linhas=file.readlines()
    print(linhas)
    for linha in linhas[1:]:
        partes=linha.strip().split(';')
        print(partes)


