import pandas as pd
import sqlite3

# Connexion à la base de données SQLite (ou création si elle n'existe pas)
connection = sqlite3.connect('import.sqlite')

# Création du curseur pour exécuter les requêtes SQL
cursor = connection.cursor()

# Lecture du fichier CSV avec pandas et encodage UTF-8
df_clients = pd.read_csv('commandes.csv', encoding='utf-8')

# Boucle pour insérer chaque ligne du DataFrame dans la base de données
for index, row in df_clients.iterrows():
    cursor.execute('''
        INSERT INTO COMMANDE (cmd_id,client_id,date_commande, montant_cmd)
        VALUES (?, ?, ?, ?)
    ''', (
        row['Commande_ID'],                 # Assurez-vous que les noms de colonnes correspondent au CSV
        row['Client_ID'],
        row['Date_Commande'],
        row['Montant_Commande']     # 0 ou 1 pour le consentement marketing
    ))

# Sauvegarde (commit) des changements dans la base de données
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()
