-- return book epub version

SELECT epub
FROM books
WHERE author = %s AND name = %s;
