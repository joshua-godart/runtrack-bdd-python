import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "DBemployes"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE DBemployes")
#mycursor.execute("CREATE TABLE employes (id int AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), "
                 #"prenom VARCHAR(255), salaire DECIMAL, id_service int)")
#mycursor.execute("CREATE TABLE services (id int AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255))")

employes = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
#val = (input("entrez le nom :"), input("entrez le prénom :"), input("entrez le salaire :"), input("entrez l'id de service :"))
#services = "INSERT INTO services (nom) VALUES (%s)"
#mycursor.execute(employes, val)
#mycursor.execute("INSERT INTO services (nom) VALUES ('RH')")
mycursor.execute("SELECT employes.nom, employes.prenom, employes.salaire, services.nom "
                 "AS service FROM employes JOIN services ON employes.id_service = services.id")
#mydb.commit()

#mycursor.execute("SELECT*FROM employes where salaire > 3000")

#result = mycursor.fetchall()

#for x in result:
    #print(x)
