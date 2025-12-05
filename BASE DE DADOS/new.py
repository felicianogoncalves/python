import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biblioteca",
    )

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(25) NOT NULL,
            autor VARCHAR(25),
            ano INT,
            disponibilidade BOOLEAN DEFAULT TRUE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def adicionar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    dis = input("Disponível? (s/n): ").lower() == "s"
    
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO livros(titulo, autor, ano, disponibilidade) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (titulo, autor, ano, dis))
    conn.commit()
    cursor.close()
    conn.close()
    print(f'Livro "{titulo}" adicionado com sucesso!')

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    print('\nLista de livros:')
    for livro in livros:
        status = "Disponível" if livro[4] else "Indisponível"
        print(f'{livro[0]} - {livro[1]} | {livro[2]} | {livro[3]} | {status}')
    cursor.close()
    conn.close()

def atualizar_dis():
    listar_livros()
    id_livro = int(input('Id do livro para atualizar: '))
    disponivel = input('Novo status - disponível? (s/n): ').lower() == 's'
    
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE livros SET disponibilidade=%s WHERE id=%s"
    cursor.execute(sql, (disponivel, id_livro))
    conn.commit()
    cursor.close()
    conn.close()
    print('Dados atualizados com sucesso!')

def apagar_livro():
    listar_livros()
    id_livro = int(input('Introduza o id do livro a remover: '))
    
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM livros WHERE id=%s"
    cursor.execute(sql, (id_livro,))
    conn.commit()
    cursor.close()
    conn.close()    
    print('Livro apagado com sucesso!')

def menu():
    criar_tabela()
    while True:
        print('\nBiblioteca')
        print('1 - Listar livros')
        print('2 - Adicionar livro')
        print('3 - Atualizar disponibilidade')
        print('4 - Apagar livro')
        print('5 - Sair')
        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            listar_livros()
        elif escolha == '2':
            adicionar_livro()
        elif escolha == '3':
            atualizar_dis()
        elif escolha == '4':
            apagar_livro()
        elif escolha == '5':
            print('Saindo...')
            break
        else:
            print('Digite uma opção entre 1 e 5')

menu()