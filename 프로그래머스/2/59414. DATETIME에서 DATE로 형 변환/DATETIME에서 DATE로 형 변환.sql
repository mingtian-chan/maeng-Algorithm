-- 코드를 입력하세요
SELECT
    ANIMAL_ID,
    NAME,
    DATE_FORMAT(
        ANIMAL_INS.DATETIME, "%Y-%m-%d"
        ) AS "날짜"
from ANIMAL_INS
ORDER BY 1
