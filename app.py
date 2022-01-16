from flask import Flask, render_template, redirect, request		#importo la classe Flask e funzioni
import sqlite3

app = Flask(__name__)
db_path = 'database.db'

@app.route('/')				#decorator che richiama il metodo route di app, definisce un percorso URL, / è la homepage
def index():
	connection = sqlite3.connect(db_path)
	connection.row_factory = sqlite3.Row								#la connessione è impostata a righe

	posts = connection.execute('SELECT * FROM posts').fetchall()		#seleziona tutto (tutte le righe) dalla tabella posts, fetchall fa si che tutte le righe siano organizzate in una lista python, poi assegnata a posts (variabile)
	connection.close()

	return render_template('index.html', posts=posts)					#il primo post è quello che sarà accessibile dal file HTML, il secondo è quello che ho creato sopra

@app.route('/<int:idx>/delete', methods=('POST',))						#è un possibile continuo della barra degli indirizzi, con /numero intero(l'id)/delete, esattamente ciò che provoca la pressione del bottone elimina
def delete(idx):														#definisco cosa succede quando viene fatta una richiesta http di tipo post a questo indirizzo
	connection = sqlite3.connect(db_path)
	connection.row_factory = sqlite3.Row

	connection.execute('DELETE FROM posts WHERE id=?', (idx,))			#cancello l'elemento con id = idx dalla tabella (? è un placeholder)
	
	connection.commit()													#salva le modifiche
	connection.close()
	return redirect('/')												#torno alla homepage

@app.route('/create', methods=('GET', 'POST'))
def create():
	if request.method == 'POST':
		titolo = request.form['titolo']
		info = request.form['info']

		connection = sqlite3.connect(db_path)
		connection.row_factory = sqlite3.Row

		connection.execute('INSERT INTO posts (titolo, info) VALUES (?, ?)', (titolo, info))	#inserisco il post nella tabella

		connection.commit()
		connection.close()
		return redirect('/')

	return render_template('create.html')