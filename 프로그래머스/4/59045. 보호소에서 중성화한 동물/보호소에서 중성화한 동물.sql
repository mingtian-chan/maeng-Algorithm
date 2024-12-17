-- 코드를 입력하세요
# 보호소에 들어올 당시에는 중성화 되지 않았지만, 
# 보호소를 나갈 당시에는 중성화 된 동물

WITH I AS (
    SELECT 
        ANIMAL_ID, 
        ANIMAL_TYPE,
        NAME
    FROM ANIMAL_INS
    WHERE SEX_UPON_INTAKE LIKE "Intact%"
)

SELECT 
    I.ANIMAL_ID,
    I.ANIMAL_TYPE,
    I.NAME
FROM I
JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE 
    SEX_UPON_OUTCOME LIKE "Spayed%" OR
    SEX_UPON_OUTCOME LIKE "Neutered%"