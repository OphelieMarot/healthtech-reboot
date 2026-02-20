# health_analyzer_v3.py

# Sécuriser le nombres de mesures
while True:
    try:
        nb_mesures = int(input("Combien de mesures veux-tu entrer ?"))
        if nb_mesures > 0:
            break
        else:
            print("Le nombre doit être supérieur à 0")

    except ValueError:
        print("Tu dois entrer un nommbre valide.")

total = 0

# Sécuriser chaque mesure
for i in range(nb_mesures):

    while True:
        try:
            mesure = int(input(f"Entre la mesure numéro {i+1} :"))

            if mesure > 0:
                total += mesure
                break
            else:
                print("La mesuere doir être positive")

        except ValueError:
            print("Tu dois entrer un nombre valide") 

# Calcul
moyenne = total / nb_mesures

print(f"La moyenne est de {moyenne} bpm")

if moyenne > 100:
    print("Fréquence cardiaque élevée")
else:
    print("Fréquence cardiaque normale")    
    