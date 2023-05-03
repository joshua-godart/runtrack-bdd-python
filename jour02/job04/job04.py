import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "LaPlateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT nom, capacite FROM salle")

result = mycursor.fetchall()

for x in result:
    print(x)