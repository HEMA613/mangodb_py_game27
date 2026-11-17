#import random
#from pymongo import MongoClient

#client = MongoClient("mongodb://localhost:27017/")
#db = client["jeumonstre"]

#collection_personnages = db["personnages"]
#collection_monstres = db["monstres"]
#______________________________________________________________________________________________________________________________

# definir la liste des options
# afficher les options numéroté
# demande de choisir une option numéroté
#        vérifier si l'option est valide
#        retourné l'option choisi

#options = ["option1", "option2", "option3"]


#def afficher_options(liste_options):
    #for numero, option in enumerate(liste_options, start=1):
       # print(f"{numero}. {option}")

   # choix = input("choisir un option ").strip()

   # if choix.isdigit():
       # index = int(choix) - 1
        #if 0 <= index < len(liste_options):
          #  return liste_options[index]

    #print("options pas valide")
   # return None


#mon_choix = afficher_options(options)
#print(f"Vous avez choisi : {mon_choix}")

# créer son equipe
#     Les informations des personnages et monstre doivent être récupérées depuis la base de donnée
#     chosir 3 personnages pour lequipe
#     choisir 3 monstres aleatoirement
#     
#def créer_equipe():
    #tous_les_personnages = list(collection_personnages.find({}, {"id":0}))
    #noms_personnages = ["noms_personnages"] 

#_____________________________________________________________________________________________________________

#Afficher Menu
# Recuperer un choix valide parmi les options
#    tant que infini
#    afficher les options numerotees
#         pour chaque option dans enumerate(options, start(=l)
#              afficher (i). (option}
#    demander un choix a l'utilisateur 
#    si le choix est valide
#       retourner le choix valide 
#    afficher un message d'erreur

def afficher_menu(options):
    while True:
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choix = input("choisir une option : ").strip()
        if choix_est_valide(choix, 1, len(options)):
            index = int(choix) - 1
            return options[index]
        print("choix invalide")

# choix est valide
#    si le choix n'est pas isdigit()
#       retourner False
#    convertir le choix en entier
#    si le choix est inférieur au minimum ou supérieur au maximum
#       retourner False
#    retourner True

def choix_est_valide(choix, minimum, maximum):
    if not choix.isdigit():
        return False

    nombre = int(choix)

    if nombre < minimum or nombre > maximum:
        return False
    return True