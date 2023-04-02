-- insert data into authors table
-- NOTE: viewscounter column is UNSIGNED

INSERT INTO authors (
    name,            -- varchar(100)      required
	birthday,        -- date              default null
	nationality,     -- varchar(15)       default null
	viewerscounter,  -- int               default null
	description,     -- text              default null
	wikilink,        -- text              default null
)
VALUES (%s, %s, %s, %s, %s, %s);
