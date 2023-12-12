--  lists all records of the table second_table with some requirements.
SELECT `score`, `name`
FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
