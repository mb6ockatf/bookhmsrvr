CREATE TABLE IF NOT EXISTS authors (
	id             SERIAL,
	name           varchar(100) NOT NULL UNIQUE,
	birthday       date         DEFAULT NULL,
	nationality    varchar(15)  DEFAULT NULL,
	viewerscounter int          DEFAULT NULL,
	description    text         DEFAULT NULL,
	wikilink       text         DEFAULT NULL,
	-- ------------------------constraints-------------------------------------
	PRIMARY KEY (id),
	CHECK (viewerscounter > 0)
);
