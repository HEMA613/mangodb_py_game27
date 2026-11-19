import random
import time
from pymongo import MongoClient

Récupérer personnages et monstres sur MongoDB
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

#creer equipe
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
#       afficher - nom du personnage

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

