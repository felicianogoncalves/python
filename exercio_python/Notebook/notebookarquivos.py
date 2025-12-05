import io # não é necessário para manipulações simples

# REGRAS IMPORTANTES
# .read(n) --> ler n caracteres e retornar uma string
# .read() --> ler todo o ficheiro e retorna uma string

# ABRIR O FICHEIRO frases.txt EM MODO DE LEITURA

with open("frases.txt", "r", encoding = "utf-8") as disparates:
    conteudo = disparates.read()
    print("Onde está o cursor?: ",disparates.tell())
    disparates.seek(0)  # meter o cursor na posição zero
    print(conteudo)
    # visualizar os 6 primeiros caracteres
    print("Primeiros 6 caracteres: ",disparates.read(6))  # por ter posto o cursor na posição zero, isto printa. No final do ficheiro não printava nada
print()

# LER VÁRIAS LINHAS DO FICHEIRO
with open("frases.txt", "r", encoding = "utf-8") as ficheiro:
    linha1 = ficheiro.readline()  # lê a primeira linha
    print("Primeira leitura: ",linha1)
    linha2 = ficheiro.readline()  # lê a segunda linha, pois o cursor movimentou-se com a anterior
    print("Segunda leitura: ",linha2)
    restantes_linhas = ficheiro.readlines()  # lê as restantes linhas depois do cursor
    print("Restantes linhas: ",restantes_linhas)
print()

# PROCESSAR LINHAS DO FICHEIRO COM UM LOOP
with open("frases.txt", "r", encoding = "utf-8") as ficheiro:
    for linha in ficheiro:
        print(linha.strip(), end=" | ")  # usamos o strip para tirar todos os espaços e parágrafos, e depois o end para separar com " | "

# ESCREVER NO FICHEIRO
# MODOS: w, a, r+
# método .write() --> escreve a string exatamente como é escrita, não acrescenta \n
with open("frases2.txt", "w", encoding = "utf-8") as ficheiro:
    ficheiro.write("Hoje é segunda-feira\n")
    ficheiro.write("Bom dia para ir ao cinema")
print()

lista_strings = ["A\n","B\n","C\n","D"]
with open("frases2.txt", "w", encoding = "utf-8") as ficheiro:
    ficheiro.writelines(lista_strings)

# split() -> dividir cada linha em palavras separadar por separadores

# with open('frases.txt','r',encoding='utf-8') as file:
#     for linha in file:
#         partes=linha.split()
#         print(partes)
#         print(partes[1])

#pedir ao ultilizador um nova entrada
nova_linha=input("Digite uma nova entrada:")
with open("frases.txt","a",encoding="utf-8") as ficheiro:
    ficheiro.write(nova_linha)
