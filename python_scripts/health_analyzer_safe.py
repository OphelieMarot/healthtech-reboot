# health_analyzer_safe.py

try:
    nb_mesures = int(input("Combien de mesures veux-tu entrer ?"))
    
    if nb_mesures <= 0:
        print(" Le nombre de mesure doit être supérieur à 0")
    else:
        total =0

        for i in range(nb_mesures):
            mesure = int(input(f"Entre la mesure numéro {i+1} :"))
            total += mesure

        moyenne = total / nb_mesures
            
        print(f"La moyenne est de {moyenne} bpm")

        if moyenne > 100:
            print("Fréquence cardiaque élevée")
        else:
            print("Fréquence cardiaque normale")

except ValueError:
    print("Erreur : tu dois entrer uniquement des nombres.")                
             

