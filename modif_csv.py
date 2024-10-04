import pandas as pd
import sqlite3

# Connexion à la base de données SQLite (ou création si elle n'existe pas)
connection = sqlite3.connect('import.sqlite')

# Création du curseur pour exécuter les requêtes SQL
cursor = connection.cursor()

# Lecture du fichier CSV avec pandas et encodage UTF-8
df_clients = pd.read_csv('jeu-clients.csv', encoding='utf-8')

# Boucle pour insérer chaque ligne du DataFrame dans la base de données
for index, row in df_clients.iterrows():
    cursor.execute('''
        INSERT INTO CLIENT (id, nom, prenom, email_client, birth, telephone, adresse, consent)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        row['Client_ID'],                 # Assurez-vous que les noms de colonnes correspondent au CSV
        row['Nom'],
        row['Prénom'],
        row['Email'],
        row['Date_Naissance'],
        row['Téléphone'],
        row['Adresse'],
        row['Consentement_Marketing']     # 0 ou 1 pour le consentement marketing
    ))

# Sauvegarde (commit) des changements dans la base de données
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()
