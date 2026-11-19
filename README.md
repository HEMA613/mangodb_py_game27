# mangodb_py_game27
base de donnée, python, mongoDb, gamecreation

# 1. Installer les dépendances
pip install pymongo
 
# Connection personnages, monstres et sauveageder le classement sur MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["jeumonstre"]

personnages_dispo = list(db["personnages"].find({}, {"_id": 0}))
monstres_dispo = list(db["monstres"].find({}, {"_id": 0}))


# 2. Lancer le jeu
python-game.py
