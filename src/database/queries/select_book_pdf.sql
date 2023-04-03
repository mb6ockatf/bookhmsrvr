-- return book pdf version

SELECT pdf
FROM books
WHERE author = %s AND name = %s;
