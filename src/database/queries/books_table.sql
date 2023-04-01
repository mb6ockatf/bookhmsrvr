CREATE TABLE IF NOT EXISTS books (
	id SERIAL PRIMARY KEY,
	name varchar(100) NOT NULL,
	author varchar(50) NOT NULL REFERENCES authors (name),
	due_date date DEFAULT NULL,
	pages smallint UNSIGNED DEFAULT NULL,
	genre varchar(20) DEFAULT NULL,
	rating char(1) DEFAULT NULL,
	viewers_counter int UNSIGNED DEFAULT 0,
	downloads_counter int UNSIGNED DEFAULT 0,
	epub bytea DEFAULT NULL,
	epub_size bigint UNSIGNED DEFAULT NULL,
	pdf bytea DEFAULT NULL,
	pdf_size bigint UNSIGNED DEFAULT NULL,
	-- same author cannot write same book twice, right?
	UNIQUE (name, author);
)
