
#FICHA 8
# Exercício 1 - Manipulação de ficheiros txt

# 1. Ler o ficheiro inteiro e mostrar no terminal
with open("relatorio.txt", "r", encoding="utf-8") as ficheiro:
    conteudo = ficheiro.read()
    print(" Conteúdo completo do ficheiro:")
    print(conteudo)

# 2. Ler o ficheiro linha a linha e imprimir cada linha
with open("relatorio.txt", "r", encoding="utf-8") as ficheiro:
    print("\n Linhas do ficheiro:")
    for linha in ficheiro:
        print(linha.strip())  # strip() remove quebras de linha extras

# 3. Contar quantas vezes a palavra "projeto" aparece
with open("relatorio.txt", "r", encoding="utf-8") as ficheiro:
    conteudo = ficheiro.read()
    ocorrencias = conteudo.lower().count("projeto")  # lower() garante que conta sem diferenciar maiúsculas/minúsculas
    print(f"\n A palavra 'projeto' aparece {ocorrencias} vezes no ficheiro.")



# 5. Acrescentar uma nova frase no final do ficheiro
with open("relatorio.txt", "a", encoding="utf-8") as ficheiro:
    ficheiro.write("\nNova frase adicionada ao relatório.")
print("\n Nova frase adicionada com sucesso!")
