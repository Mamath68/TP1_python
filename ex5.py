nombre = int(input("Entre un nombre entier, svp : "))

estpair = ('pair', 'impair')
estpositif = ('zéro', 'positif', 'négatif')

if nombre == 0:
    print("Le nombre est null et pair ...")
else:
    print(f"Le nombre est {estpositif[int(nombre / abs(nombre))]} et {estpair[nombre % 2]} ")
