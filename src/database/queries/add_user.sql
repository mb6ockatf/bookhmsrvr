-- insert data into users table
-- NOTE: nickname is set to be unique

INSERT INTO users (
    nickname,      -- varchar(32) required
	name,          -- varchar(32) default null
	surname,       -- varchar(15) default null
	email,         -- varchar(32) default null
	passwordhash,  -- varchar(32) default null
	duedate,       -- date        default null
)
VALUES (%s, %s, %s, %s, %s, %s);
