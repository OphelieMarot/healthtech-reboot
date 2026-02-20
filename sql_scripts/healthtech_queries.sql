-- ====================================
-- HealthTech Project SQL Queries
-- Author: Ophélie Marot
-- Date: 2026-02-20
-- ====================================

-- 1 Création de la table patients
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    age INT,
    frequence-cardiaque INT
);

-- 2 Insertion de données réalistes
INSERT INTO patients (nom, age,
frequence_cardiaque)
VALUES
('Alice', 34, 72),
('Bob', 67, 88),
('Claire', 75, 95),
('David', 52, 60),
('Emma', 81, 102),
('Farid', 29, 55);

--3 Sélectionde toutes les données
SELECT * FROM patients
WHERE age > 70;

--4 Moyenne de la fréquence cardiaques
SELECT AVG(frequence_cardiaque) AS moyenne_fc FROM patients;

--5 Patients de plus de 70 ans
SELECT * FROM patients
WHERE age > 70;

--6 Top 3 fréquences cardiaques les plus élevées 
SELECT * FROM patients
ORDER BY frequence_cardiaque DESC
LIMIT 3;

--7 Sous requête pour trouver le patient avec la fréquence cardiaque maximal
SELECT nom, frequence_cardiaque
FROM patients
WHERE frequence_cardiaque = (
    SELECT MAX(frequence_cardiaque)
    FROM Patients
);

--8 Patient le plus jeune (nom et age)
SELECT nom, age
FROM patients
ORDER BY patients ASC
LIMIT 1;

--9 Patient le plus agé (nom, age et fréquence cardiaque)
SELECT nom, frequence_cardiaque, age
FROM patients
ORDER BY patient DESC
LIMIT 1;

--10 Moyenne et nombre de patients avec age > 50
SELECT COUNT(*) AS nb_patients,
AVG(frequence_cardiaque) AS moyenne_fc
FROM patients
WHERE age > 50;