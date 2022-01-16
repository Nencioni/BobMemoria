DROP TABLE IF EXISTS posts;

CREATE TABLE posts(
	id INTEGER PRIMARY KEY AUTOINCREMENT,			/*definisco un id univoco di ogni post, univoco grazie a primary key, che si aggiorna automaticamente*/
	titolo TEXT,
	info TEXT
);

INSERT INTO posts(titolo, info) VALUES(
	'Venera il Rizzo',
	'Senza di lui non sarei qui'
);
INSERT INTO posts(titolo, info) VALUES(
	'Insulta Curry',
	'Per la sua esistenza e anche per il fatto che giochi a LOL'
);
INSERT INTO posts(titolo, info) VALUES(
	'Prega che in quinta non arrivi il Mariotti al posto del Maurone',
	'Cazzo leggi prega'
);