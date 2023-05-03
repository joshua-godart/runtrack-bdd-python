import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "LaPlateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * From etudiants")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
