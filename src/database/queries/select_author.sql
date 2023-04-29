SELECT name, birthday, nationality,
  viewscounter, description, wikilink
FROM authors
WHERE name = %s;
