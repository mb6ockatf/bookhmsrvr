CREATE TABLE IF NOT EXISTS reviews (
	id             SERIAL,
	authornickname varchar(32)    NOT NULL     REFERENCES users (nickname),
	duedate        date           NOT NULL,
	stars          char(1)        NOT NULL,
	contents       varchar(10000) NOT NULL,
	-- ------------------------constraints-------------------------------------
	PRIMARY KEY (id)
);
