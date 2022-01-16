#initialize database
import sqlite3

connection = sqlite3.connect('database.db')		#oggetto che rappresenta la connessione al database
with open('crea_posts.sql') as f:
	connection.executescript(f.read())			#esegue lo script letto nel file
connection.commit()								#salva le modifiche
connection.close()