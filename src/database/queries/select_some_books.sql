-- select a list of books

SELECT name, author, language
FROM books
ORDER BY rating DESC
LIMIT 15;
