# health_analyser.py

nb_mesures = int(input("Combien de mesures de fréquence cardiaque veux-tu entrer ?"))

total = 0

for i in range(nb_mesures):
    mesure = int(input(f"Entre la mesure numéro {i+1} :"))
    total = total + mesure

moyenne = total / nb_mesures

print(f"La moyenne est de {moyenne} bpm")

if moyenne > 100:
    print(" Fréquence vardiaque élevée")
else:
    print("fréquence cardiaque normale")    