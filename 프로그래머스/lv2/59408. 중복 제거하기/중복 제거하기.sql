-- 코드를 입력하세요
SELECT  COUNT(NAME)
FROM    (
        SELECT DISTINCT NAME
        FROM    ANIMAL_INS
        ) AS TEMP