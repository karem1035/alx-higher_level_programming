-- a script that lists all the cities of California
USE hbtn_0d_usa;

SELECT id, name
FROM STATES
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California')
ORDER BY id;

