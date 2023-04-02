-- select information about book

SELECT author,
    duedate,
    language,
    pages,
    description,
    wikilink,
    rating,
    viewerscounter,
    downloadscounter,
    epubsize,
    pdfsize
FROM books
WHERE name = %s AND author = %s;
