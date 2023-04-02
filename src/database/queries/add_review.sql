-- insert data into reviews table
-- NOTE: authornickname column references users (nickname)

INSERT INTO reviews (
    authornickname,  -- varchar(32)  required
	duedate,         -- date         default null
	stars,           -- varchar(15)  default null
	contents,        -- int          default null
)
VALUES (%s, %s, %s, %s);
