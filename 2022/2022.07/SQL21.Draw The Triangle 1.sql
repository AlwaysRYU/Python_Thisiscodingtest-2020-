# Draw The Triangle 1

# 문제
별찍기 문제

# 풀이
SET @NUMBER = 21;

SELECT REPEAT('* ', @NUMBER := @NUMBER - 1)
FROM INFORMATION_SCHEMA.TABLES LIMIT 20;