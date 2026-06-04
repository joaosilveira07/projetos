import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jujyo9",
        database="ladpy2"
    )

