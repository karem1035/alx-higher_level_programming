-- a script that lists all the cities of California
USE hbtn_0d_usa;

SELECT *
FROM states
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

