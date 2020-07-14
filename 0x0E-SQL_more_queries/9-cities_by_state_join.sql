-- task 9
-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT c.id, c.name, s.name FROM cities AS c, states AS s
WHERE c.state_id = s.id
ORDER BY c.id ASC;
