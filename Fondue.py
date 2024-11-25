# Déclaration des constantes et variables de base
BASE = 4
fromage = 800  # en grammes
eau = 2  # en décilitres
ail = 2  # en gousses
pain = 400  # en grammes

# Demande à l’utilisateur d’introduire le nombre de convives
nbConvives_input = input("Entrez le nombre de personne(s) conviées à la fondue : ")

# Vérifier si l’utilisateur n’a rien entré
if nbConvives_input.strip() == "":
    nbConvives = BASE
else:
    nbConvives = int(nbConvives_input)

# Calcul des nouvelles quantités en fonction du nombre de convives
nouveau_fromage = fromage * nbConvives / BASE
nouvelle_eau = eau * nbConvives / BASE
nouvel_ail = ail * nbConvives / BASE
nouveau_pain = pain * nbConvives / BASE

# Affichage de la recette adaptée
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {int(nouveau_fromage)} gr de fromage")
print(f"- {int(nouvelle_eau)} dl d'eau")
print(f"- {int(nouvel_ail)} gousse(s) d'ail")
print(f"- {int(nouveau_pain)} gr de pain")
