from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["jeumonstre"]


# definir la liste des options
# afficher les options numéroté
# demande de choisir une option numéroté
#        vérifier si l'option est valide
#        retourné l'option choisi

options = ["option1", "option2", "option3"]


def afficher_options(liste_options):
    for numero, option in enumerate(liste_options, start=1):
        print(f"{numero}. {option}")

    choix = input("choisir un option ").strip()

    if choix.isdigit():
        index = int(choix) - 1
        if 0 <= index < len(liste_options):
            return liste_options[index]

    print("options pas valide")
    return None


mon_choix = afficher_options(options)
print(f"Vous avez choisi : {mon_choix}")

# créer son equipe
#     chosir 3 joueur pour lequipe
#     
def créer_equipe():

