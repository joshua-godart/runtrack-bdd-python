job22:
	select nom, prenom, age, email from etudiants where age = (select min(age) from etudiants);