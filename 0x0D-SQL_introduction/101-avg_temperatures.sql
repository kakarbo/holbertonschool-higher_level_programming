-- that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- DML Instrution
SELECT city AVG(value) AS avg_tempname FROM $temperatures WHERE name IS NOT NULL ORDER BY score DESC;
