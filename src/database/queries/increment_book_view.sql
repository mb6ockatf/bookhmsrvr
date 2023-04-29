-- increment book page views counter

UPDATE books
SET viewerscounter = viewerscounter + 1
WHERE name = %s AND author = %s;
