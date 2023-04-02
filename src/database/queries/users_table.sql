CREATE TABLE IF NOT EXISTS users (
	id           SERIAL,
	nickname     varchar(32) NOT NULL UNIQUE,
	name         varchar(32) DEFAULT NULL,
	surname      varchar(32) DEFAULT NULL,
	email        varchar(32) DEFAULT NULL,
	passwordhash varchar(21) NOT NULL,
	duedate      date        NOT NULL,
	-- ------------------------constraints-------------------------------------
	PRIMARY KEY (id, nickname)
);
