-- the GROUP BY keyword to enhance query
SELECT DISTINCT score, count(score) AS number
FROM second_table
GROUP BY score;
