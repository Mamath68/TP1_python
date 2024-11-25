x = float(input("Entrez un nombre réel : "))

if (2 <= x < 3) or (0 < x <= 1) or (-10 <= x < -2):
    print(f"{int(x)} appartient à I")
else:
    print(f"{int(x)} n'appartient pas à I")
