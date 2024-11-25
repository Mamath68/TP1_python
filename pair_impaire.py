nombre = int(input("Entrez un nombre entier : "))

# Vérifier si le nombre est positif, négatif ou zéro
if nombre > 0:
    signe = "positif"
elif nombre < 0:
    signe = "négatif"
else:
    signe = "zéro (et il est pair)"

# Vérifier si le nombre est pair ou impair
if nombre != 0:
    if nombre % 2 == 0:
        parite = "pair"
    else:
        parite = "impair"
else:
    parite = ""

# Afficher le résultat
if nombre == 0:
    print(f"Le nombre est {signe}")
else:
    print(f"Le nombre est {signe} et {parite}")
