-- that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- DML Instrution
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp  <= 3 DESC;
