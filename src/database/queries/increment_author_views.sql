-- increment author page views counter

UPDATE authors
SET viewerscounter = viewerscounter + 1
WHERE id = %s AND name = %s;
