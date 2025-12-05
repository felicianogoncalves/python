# Testar a ligação com a base de dados: employees (Workbench)
import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employees"
    )
    print("Conexão estabelecida")

except mysql.connector.Error as e:
    print(f'erro {e}')

cursor= conn.cursor()
cursor.execute('SELECT * FROM departments')
for dep in cursor.fetchall(): # retorna uma lista de tupulas
    print(dep)