import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "LaPlateforme"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE etage (id int AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), numero int, superficie int)")
#mycursor.execute("CREATE TABLE salle (id int AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), id_etage int, capacite int)")

#mycursor.execute("SHOW TABLES")

#result = mycursor.fetchall()

#for x in result:
  #print(x)