job12:
	insert into etudiants (nom, prenom, age, email) values ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');
	select id, nom, prenom, age, email from etudiants where nom = 'Dupuis';