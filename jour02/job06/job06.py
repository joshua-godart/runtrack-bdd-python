import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "LaPlateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT sum(capacite) FROM salle")

result = mycursor.fetchone()

for x in result:
    print("La capacité de toute les salles est de :", x)