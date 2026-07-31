-- Lists all records with a non-empty name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
