-- that displays the max temperature of each state (ordered by State name).
-- DML Instrution
SELECT state, MAX(value) AS avg_temp FROM temperatures WHERE month IN (A, Z) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
