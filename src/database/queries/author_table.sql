CREATE TABLE IF NOT EXISTS authors (
	id SERIAL PRIMARY KEY,
	name varchar(100) NOT NULL UNIQUE,
	birthday date DEFAULT NULL,
	nationality varchar(15) DEFAULT NULL,
	viewerscounter int UNSIGNED DEFAULT NULL,
	description text DEFAULT NULL,
	wikilink text DEFAULT NULL;
)
