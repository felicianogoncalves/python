import mysql.connector
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database ="biblioteca",
    )

#criar a tabela

def criar_tabela():
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS livros(id INT AUTO_INCREMENT PRIMARY KEY,titulo VARCHAR(25) NOT NULL,autor VARCHAR(25),ano INT,disponibilidade BOOLEAN DEFAULT TRUE)")
    conn.commit()
    cursor.close()
    conn.close()

#def adicionar livro()

def adicionar_livro():
    titulo=input("titulo:")
    autor=input("Autor:")
    ano=int(input("Ano:"))
    dis=input("Disponivel?(s/n):").lower()=="s"
    conn=conectar()
    cursor=conn.cursor()
    sql="INSERT INTO livros(titulo,autor,ano,dis) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (titulo,autor,ano,dis))
    conn.commit()
    cursor.close()
    conn.close()
    print(f'Livros {titulo} adicionado com sucesso')

#listar todos os livros que estão na BD

def listar_livros():
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros=cursor.fetchall() # retornar em uma lista de tuplas
    print('\nLista de livros:')
    for livro in livros:
        status="Disponivel" if livro[4] else "indisponivel"
        print(f'{livro[0]} - {livro[1]} | {livros[2]} | {livro[3]} | {status}')
    cursor.close()
    conn.close()

#def atualizar disponibilidade

def atualizar_dis():
    listar_livros()
    id_livro=int(input('Id do livro para atualizar:'))
    disponivel=input('Novo status - disponivel? (s/n):').lower()=='s'
    conn=conectar()
    cursor=conn.cursor()
    sql="UPDATE livros SET dis=%s WHERE id =%s"
    cursor.execute(sql,(disponivel,id_livro))
    conn.commit()
    cursor.close()
    conn.close()
    print('Dados atualizados com sucesso')
    
#apagar um livro

def apagar_livro():
    listar_livros()
    id_livros=int(input('Introduza o id do licro a remover:'))
    conn=conectar()
    cursor=conn.cursor()
    sql="DELETE FROM livro WHERE id=%s"
    cursor.execute(sql,(id_livros))
    conn.commit()
    cursor.close()
    conn.close()    
    print('Apagado com sucesso')

#Criar menu():
def menu():
    criar_tabela()
    while True:
        print('Biblioteca')
        print('1-Listar id livros')
        print('2-Adicionar livro')
        print('3-Atualizar disponibilidade')
        print('4-Apagar')
        print('5-Sair')
        escolha=input('escolha opção:')
        if escolha =='1':
            listar_livros()
        elif escolha =='2':
            adicionar_livro()
        elif escolha =='3':
            atualizar_dis()
        elif escolha =='4':
            apagar_livro()
        elif escolha=='5':
            print('Saindo...')
            break
        else:
            print('Digite entre 1 e o 5')


menu()