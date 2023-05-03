import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "LaPlateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT sum(superficie) FROM etage")

result = mycursor.fetchone()

for x in result:
    print("La superficie de la Plateforme est de", x, "m²")