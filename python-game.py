import random
import time
from pymongo import MongoClient

# 1. Récupérer personnages et monstres sur MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["nom_de_ta_base"]  # À remplacer par le nom de votre base

personnages_dispo = list(db["personnages"].find({}, {"_id": 0}))
monstres_dispo = list(db["monstres"].find({}, {"_id": 0}))


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
# connecter mango db
#recuperer personnage et monstres sur mongo db
# 
#
#entrer le peuso du jouer 
#   tant que le peuso pas valide ressayez
#         Affichage un message d'erreur et redemander le pseudo
#Affichage des personnages disponibles
#créé une liste vide 'equipe'

# Le joueur choisit 3 personnages différents :
#   tant que longueur de 'equipe' < 3 :
#       demander un choix de personnage
#       vérifier que la saisie est un nombre (isdigit)
#       si saisie valide :
#           convertir en entier et vérifier que le numéro existe dans la liste
#           vérifier que le personnage n'est pas déjà dans 'equipe'
#               ajouter le personnage à 'equipe'
#               afficher que le personnage a été ajouté à la liste
#       sinon :
#           afficher une erreur (saisir un nombre valide de la liste)

# Vérification et affichage de l'équipe créée :
#   afficher les 3 personnages choisis

# creation vague 
#      


#systeme de combat
#   initialiser le compteur de vague a 0
def debut_vague():
#enregistrer l'heure de départ : debut_vague = time.time()
#   affrontement en boucle jusqu' a la defaite
while True:

   temps_ecoule =
   aucun_monstres =


#vérifier si on passe à la vague suivante :
#   condition 1 : temps_ecoule >= duree_vague
#                temps_ecoule >= duree_vague or incrémenter vagues += 1 :
#   condition 2 : aucun monstre vivant dans monstres_en_jeu
#creer monstres en jeu
#  si condition 1 ou condition 2 :
#     incrémenter vagues += 1 
#     réinitialiser debut_vague = time.time()
#     tirer un nouveau monstre  et l'ajouter à monstres_en_jeu
#   afficher "Vague X !"
print(f"- {perso['nom']}")
#chaque personnage possede des point de vie + povoir recuperer sur mango db
#   verifier si il reste encore des monstre au moins 1 vivant
#             tant que les monstres pv > 0 equipe monstres vivant
#    verifier si il reste encore des personnage au moins 1 vivant
#             tant que les personnage pv > 0 equipe personnage est vivant
#          sinon personnage attacque toujour en 1er



#classement des meilleurs scores
#  verifier si victiore 
#       mise a jour du score et sauvegarde dans la base de données + nom du joueur

#classement des joueur
#  verifier si defaite
#       mise a jour de nombre de vagues + survecues + nom du joueur et sauvegarder dans la base de donnees






