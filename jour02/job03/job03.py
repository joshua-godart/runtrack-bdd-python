import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "LaPlateforme"
)

mycursor = mydb.cursor()

etage = "INSERT INTO etage (nom, numero, superficie) VALUES (%s, %s, %s)"
val = (input("entrez le nom de l'étage :"), input("entrez le numéro :"), input("entrez la superficie :"))
#mycursor.execute("delete from etage where id > 1")
salle = "INSERT INTO salle (nom, id_etage, capacite) VALUES (%s, %s, %s)"
#val2 = (input("entrez le nom de la salle :"), input("entrez l'id de l'étage :"), input("entrez la capacité :"))

mycursor.execute(etage, val)
#mycursor.execute(salle, val2)
mydb.commit()

#mycursor.execute("SELECT * From etage")
#mycursor.execute("SELECT * From salle")

#myresult = mycursor.fetchall()

#for x in myresult:
    #print(x)



