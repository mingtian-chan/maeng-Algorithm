-- 코드를 입력하세요
WITH RECURSIVE TIME AS 
(
    SELECT  0 AS HOUR
        UNION ALL
    SELECT  HOUR + 1 
    FROM    TIME
    WHERE   HOUR < 23
)  
SELECT  T.HOUR, COALESCE(COUNT(HOUR(A.DATETIME)),0) AS "COUNT"
FROM    TIME T LEFT JOIN ANIMAL_OUTS A ON T.HOUR = HOUR(A.DATETIME)
GROUP   BY T.HOUR
ORDER   BY T.HOUR;