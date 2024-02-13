-- the GROUP BY keyword to enhance query
SELECT DISTINCT score,
COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC;
