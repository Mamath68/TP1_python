# Demander à l'utilisateur d'entrer les heures de début et de fin de location
heure_debut = int(input("Donnez l’heure de début de la location (un entier) : "))
heure_fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

# Vérifier la validité des heures entrées
if heure_debut < 0 or heure_debut > 24 or heure_fin < 0 or heure_fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
elif heure_debut == heure_fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
elif heure_debut > heure_fin:
    print("Attention ! le début de la location est après la fin ...")
else:
    # Calculer le coût de la location
    cout_total = 0
    heures_tarif_1 = 0
    heures_tarif_2 = 0

    for heure in range(heure_debut, heure_fin):
        if 0 <= heure < 7 or 17 <= heure < 24:
            cout_total += 1.50
            heures_tarif_1 += 1
        elif 7 <= heure < 17:
            cout_total += 2.40
            heures_tarif_2 += 1

    # Afficher le détail de la location
    print("Vous avez loué votre vélo pendant")
    if heures_tarif_1 > 0:
        print(f"{heures_tarif_1} heure(s) au tarif horaire de 1.50 euro(s)")
    if heures_tarif_2 > 0:
        print(f"{heures_tarif_2} heure(s) au tarif horaire de 2.40 euro(s)")
    print(f"Le montant total à payer est de {cout_total} euro(s).")
