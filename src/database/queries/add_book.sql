-- insert data into books table
-- NOTE: author column references authors(name)
-- NOTE: name and author are unique names, so same author
-- cannot write same book twice

INSERT INTO books (
    name,              -- varchar(100)      required
	author,            -- varchar(50)       required
	duedate,           -- date              default null
	language,          -- char(2)           default null
	pages,             -- smallint unsigned default null
	genre,             -- varchar(20)       default null
	description,       -- text              default null
	wikilink,          -- text              default null
	rating,            -- char(1)           default null
	viewerscounter,    -- int unsigned      default 0
	downloadscounter,  -- int unsigned      default 0
	epub,              -- bytea             default null
	epubsize,          -- bigint unsigned   default 0
	pdf,               -- bytea             default null
	pdfsize            -- bigint unsigned   default 0
)
VALUES (
	%(name)s,
	%(author)s,
	%(duedate)s,
	%(language)s,
	%(pages)s,
	%(genre)s,
	%(description)s,
	%(wikilink)s,
	%(rating)s,
	%(viewerscounter)s,
	%(downloadscounter)s,
	%(epub)s,
	%(epubsize)s,
	%(pdf)s,
	%(pdfsize)s
);
