# health_analyzer_pro.py

# 1. Validation du nombre de mesures
while True:
    try:
        nb_mesures = int(input("Combien de mesures veux-tu entrer?"))
        if nb_mesures > 0:
            break
        else:
            print("Le nombre doit être superieur à 0")

    except ValueError:
        print("Tu dois entrer un nombre valide.")

# 2. Initialisation
total = 0
mesures = []

# 3. Entrée sécurisée de chaque mesure
for i in range(nb_mesures):
    while True:
        try:
            mesure = int(input(f"Entre la mesure numéro {i+1}:"))
            if mesure > 0:
                mesures.append(mesure)
                total += mesure
                break
            else:
                print("La mesure doit être positive.")

        except ValueError:
            print("tu dois entrer un nombre valide.")

# 4. Calculs
moyenne = total / nb_mesures
minimum = min(mesures)
maximum = max(mesures) 

# 5. Rapport final
print("\n===== RAPPORT FREQUENCE CARDIAQUE =====")
print(f"Nombre de mesures : {nb_mesures}")
print(f"Mesures enregistrées : {mesures}")
print(f"Moyenne : {moyenne:.2f} bpm")
print(f"Minimum : {minimum} bpm")
print(f"Maximum : {maximum} bpm")

if moyenne > 100:
    print("Fréquence cardiaque élevée")
else:
    print("Fréquence cardiaque normale")    