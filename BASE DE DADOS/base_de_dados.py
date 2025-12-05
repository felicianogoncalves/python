import mysql.connector

# 1- conexão inicial ao mysql

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        #database ="employees",
    )
print("Conexão estabelecida")

#criar objeto cursor
cursor=conn.cursor()

#criar Base de dados
cursor.execute(
    "CREATE DATABASE IF NOT EXISTS biblioteca")
print("Base de dados criada")

#fechar esta conexão
cursor.close()
conn.close()

#reconectar-me mas desta vez à bd biblioteca 
conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database ="biblioteca",
    )
print("Conexão estabelecida à db biblioteca")

#criar um tabela livros
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS livros(id INT AUTO_INCREMENT PRIMARY KEY,titulo VARCHAR(25) NOT NULL,autor VARCHAR(25),ano INT,disponibilidade BOOLEAN DEFAULT TRUE)"
)

#Inserir um livro

livros=[("O sr ANEIS","Tolkien",1954,True),
        ("Biblia","Consorcio",100,True)]
sql="INSERT INTO livros(titulo,autor,ano,disponibilidade) VALUES (%s,%s,%s,%s)" # o %s vai ver estes pontos como dados e nao como string
cursor.executemany(sql,livros)

conn.commit()
#Encerrar        
cursor.close()
conn.close()

#eliminar
#cursor.execute("DROP DATABASE biblioteca")