# Se importa la base de datos
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass"
)

print(mydb)