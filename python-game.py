# definir la liste des options 
# afficher les options numéroté
# demande de choisir une option numéroté
#        vérifier si l'option est valide
#        retourné l'option choisi
#
#           

options = ["option1", "option2", "option3"]
def afficher_options (liste_options):
    for numero, option in enumerate(liste_options, start=1):
        print(f"{numero}. {option}")

choix = input("choisir un option ")

if choix.isdigit():
    index = int(choix) -1
    if 0 

    

    

