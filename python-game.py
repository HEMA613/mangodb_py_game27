import random
import time
from pymongo import MongoClient

#Récupérer personnages et monstres sur MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["jeumonstre"]

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

def est_choix_valide(choix, minimum, maximum):
    if not choix.isdigit():
        return False
    choix = int(choix)
    if choix < minimum or choix > maximum:
        return False
    return True

#entrer le pseudo du joueur
#   tant que infini
#       demander au joueur d'entrer son pseudo
#       si le pseudo est valide
#           retourner le pseudo
#       afficher un message d'erreur et redemander le pseudo

#pseudo est valide
#   enlever les espaces au début et à la fin
#   si le pseudo est vide
#       retourner false
#   retourner true


#afficher personnages
#   créer une liste vide 'noms'
#   pour chaque personnage dans la liste
#       ajouter le nom du personnage dans 'noms'
#   afficher les options numerotees de 'noms'

#créer equipe
#   créer une liste vide 'equipe'
#   créer une copie de personnages_dispo 
#   tant que l'equipe n'est pas complète =3
#       afficher les personnages restants
#       demander un choix de personnage
#       si le choix est valide (entre 1 et le nombre de restants)
#           retirer de 'restants' le personnage choisi -1
#           ajouter ce personnage à 'equipe'
#           afficher que le personnage a été ajouté
#       sinon
#           afficher une erreur (saisir un nombre valide de la liste)
#   retourner l'equipe

#afficher l'equipe
#   afficher "Votre équipe :"
#   pour chaque personnage dans equipe
#       afficher le nom du personnage



#choisir les monstres
#   créer une liste vide 'monstres_en_jeu'
#   tant que la longueur de 'monstres_en_jeu' est inférieure à 3
#       tirer un monstre avec random.choice
#       si le monstre n'est pas déjà dans 'monstres_en_jeu'
#           ajouter le monstre à 'monstres_en_jeu'
#   retourner monstres_en_jeu

#afficher les monstres
#   afficher "Monstres en jeu :"
#   pour chaque monstre dans monstres_en_jeu
#       afficher le nom du monstre

#liste des vivants
#   créer une liste vide 'vivants'
#   pour chaque personnage dans la liste
#       si sa vie est supérieure à 0
#           ajouter le personnage à 'vivants'
#   retourner vivants

#attaquer
#   choisir au hasard une cible dans les vivants de la liste cible
#   calculer les degats : attaque de l'attaquant moins defense de la cible
#   si les degats sont inférieurs à 1
#       les degats valent 1 (toujours au moins 1 point de dégât)
#   enlever les degats à la vie de la cible
#   afficher "attaquant attaque cible (-degats pv)"

#afficher la vague
#   calculer le nombre de monstres morts : 3 - monstres vivants
#   si morts = 0 : afficher "Vague 1 !"
#   si morts = 1 : afficher "Vague 2 !"
#   si morts = 2 : afficher "Round final !"

#lancer combat
#   initialiser vague_affichee à -1
#   tant qu'il reste au moins 1 personnage vivant et au moins 1 monstre vivant
#       calculer morts = 3 - nombre de monstres vivants
#       si morts est différent de vague_affichee
#           afficher la vague
#           vague_affichee = morts
#       chaque personnage vivant attaque un monstre en premier
#       chaque monstre vivant attaque un personnage
#   retourner vrai si il reste au moins 1 personnage vivant = victoire

#sauvegarder victoire
#   enregistrer dans la bdd : pseudo + résultat de victoire

#sauvegarder defaite
#   calculer le nombre de monstres morts : 3 - monstres vivants
#   enregistrer dans la bdd : pseudo + résultat de défaite + monstres morts

#afficher le classement
#   pour chaque score dans la base de données
#       afficher pseudo, résultat et monstres morts

#jouer
#   demander le pseudo
#   créer l'équipe et l'afficher
#   choisir les monstres et les afficher
#   lancer le combat
#   si victoire
#       afficher Victoire  et sauvegarder la victoire
#   sinon
#       afficher Défaite et sauvegarder la défaite
#   afficher le classement