import random

# Générer un nombre aléatoire entre 0 et 100
nombre_aleatoire = random.randint(0, 100)

# Déterminer le résultat du lancer de la pièce
if nombre_aleatoire < 50:
    resultat = "Pile !"
else:
    resultat = "Face !"

# Afficher le résultat
print(f"Résultat du lancer de la pièce : {resultat}")
