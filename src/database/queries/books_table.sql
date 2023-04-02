CREATE TABLE IF NOT EXISTS books (
	id                SERIAL,
	name              varchar(100) NOT NULL,
	author            varchar(50)  NOT NULL
	REFERENCES authors (name) ON DELETE SET NULL (author),
	duedate           date         DEFAULT NULL,
	language          char(2)      DEFAULT NULL,
	pages             smallint     DEFAULT NULL,
	genre             varchar(20)  DEFAULT NULL,
	description       text         DEFAULT NULL,
	wikilink          text         DEFAULT NULL,
	rating            char(1)      DEFAULT NULL,
	viewerscounter    int          DEFAULT 0,
	downloadscounter  int          DEFAULT 0,
	epub              bytea        DEFAULT NULL,
	epubsize          bigint       DEFAULT NULL,
	pdf               bytea        DEFAULT NULL,
	pdfsize           bigint       DEFAULT NULL,
	-- ------------------------constraints-------------------------------------
	PRIMARY KEY (id),
	-- same author cannot write same book twice, right?
	UNIQUE (name, author),
	CHECK (pages            > 0),
	CHECK (viewerscounter   > 0),
	CHECK (downloadscounter > 0),
	CHECK (epubsize         > 0),
	CHECK (pdfsize          > 0)
);
