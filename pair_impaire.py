nombre = int(input("Entrez un nombre entier : "))

if nombre > 0:
    signe = "positif"
elif nombre < 0:
    signe = "négatif"
else:
    signe = "zéro (et il est pair)"

if nombre != 0:
    if nombre % 2 == 0:
        parite = "pair"
    else:
        parite = "impair"
else:
    parite = ""

if nombre == 0:
    print(f"Le nombre est {signe}")
else:
    print(f"Le nombre est {signe} et {parite}")
