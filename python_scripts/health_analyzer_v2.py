# health_analyzer_v2

while True:
    try:
        nb_mesures = int(input("Combien de mesures veux-tu entrer ?"))

        if nb_mesures > 0:
            break
        else:
            print("Le nombre doit être supérieur à 0.")

    except ValueError:
        print("Tu dois mettre un nombre valide.")

print("Nombre validé :", nb_mesures)        