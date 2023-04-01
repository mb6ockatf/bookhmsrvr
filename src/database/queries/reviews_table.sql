CREATE TABLE IF NOT EXISTS reviews (
	id SERIAL PRIMARY KEY,
	authornickname varchar(32) NOT NULL REFERENCES authors (nickname),
	duedate date NOT NULL,
	stars char(1) NOT NULL,
	contents varchar(10000) NOT NULL;
)


