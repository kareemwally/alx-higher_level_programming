-- that script is to get AVG temperature of city
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
