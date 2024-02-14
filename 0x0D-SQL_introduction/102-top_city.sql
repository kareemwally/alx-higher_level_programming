-- that script is get the max 3
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 'August' OR month = 'July'
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;
