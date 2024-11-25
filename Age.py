from datetime import datetime

age = int(input("Quelle est votre âge ? : "))
annee = datetime.now().year - age
print("Vous avez ", age, "ans, vous êtes née en", annee)
