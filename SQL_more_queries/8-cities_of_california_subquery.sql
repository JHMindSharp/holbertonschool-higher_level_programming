-- Lists all the cities of California in the database hbtn_0d_usa.
SELECT c.id, c.name FROM cities AS c
JOIN states AS s ON c.state_id = s.id
WHERE s.name = 'California'
ORDER BY c.id ASC;
