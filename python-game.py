#Afficher Menu
#Recuperer un choix valide parmi les opions
#   tant que infini
#        afficher les options numerotees
#            pour chaque option dans enumerate(options, start=1)
#                afficher {i}. {option}
#        demander un choix a l'utilisateur
#        si le choix est valide
#           retourner le choix valide
#        afficher un message d'erreur


#choix est valide
#   si le choix n'est pas isdigit()
#      retourner false
#   convertir le choix en entier
#   si le choix est inférieur au minimum ou supérieur au maximum
#      retourner false
#retourner true

def recuperer_choix_utilisateur(options):
    while True:
        afficher_options_numerotees(options)
        choix = input("entrer votre choix")
        if est_choix_valide(choix, 1, len(options)):
            return int(choix)
        print("invalide ressayer")

def afficher_options_numerotees(options):
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def est_choix_valide()

#Création d'équipe
#recuperer personnage et monstres sur mongo db
#entre le peuso du jouer
#créé une liste vide 'equipe'
#le joueur peut chosir 3 personnage jouable du liste different
#demande 3 choix personnage valide
#afficher les 3 personnage choisi
#choisir aleatoirement 3 monstres different random.choice
#afficher les 3 monstres choisi aleatoirement

#systeme de combat
#initialiser le compteur de vague a 0
#enregistrer l'heure de départ : debut_vague = time.time()
#affrontement en boucle jusqu' a la defaite
#vérifier si on passe à la vague suivante :
#condition 1 : temps_ecoule >= duree_vague
#condition 2 : aucun monstre vivant dans monstres_en_jeu
#si condition 1 ou condition 2 :
#incrémenter vagues += 1
#réinitialiser debut_vague = time.time()
#tirer un nouveau monstre  et l'ajouter à monstres_en_jeu
#afficher "Vague X !"
#si montres meure avant la fin du temps lautre monstres enchaine
#chaque personnage possede des point de vie + povoir recuperer sur mango db
#verifier si il reste encore des monstre au moins 1 vivant
#tant que les monstres pv > 0 equipe monstres vivant
#verifier si il reste encore des personnage au moins 1 vivant
#tant que les personnage pv > 0 equipe personnage est vivant
#personnage attacque toujour en 1er
#si defaite
#mise a jour de nombre de vagues + survecues + nom du joueur et sauvegarder dans la base de donnees



#classement des meilleurs scores
#si victiore 
#mise a jour du score et sauvegarde dans la base de données + nom du joueur
