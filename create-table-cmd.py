import sqlite3

# Initialisation de la connexion à la base de données
conn = sqlite3.connect('import.sqlite')

# Création du curseur à partir de la connexion
c = conn.cursor()

# Activer les clés étrangères
c.execute("PRAGMA foreign_keys = ON")

# Ajout de la table Commande avec une clé étrangère sur Clients.id
c.execute("""
CREATE TABLE IF NOT EXISTS COMMANDE (
    cmd_id INTEGER PRIMARY KEY AUTOINCREMENT,     -- Clé primaire pour identifier la commande
    client_id INTEGER,                            -- Clé étrangère qui fait référence à CLIENT.id
    date_commande DATETIME NOT NULL,
    montant_cmd REAL NOT NULL,
    FOREIGN KEY (client_id) REFERENCES CLIENT(id) ON DELETE CASCADE
)
""")

# Sauvegarde des changements et fermeture de la connexion à la base de données
conn.commit()
conn.close()
