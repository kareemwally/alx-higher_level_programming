-- that script to get the max value of temperature
SELECT state ,MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
