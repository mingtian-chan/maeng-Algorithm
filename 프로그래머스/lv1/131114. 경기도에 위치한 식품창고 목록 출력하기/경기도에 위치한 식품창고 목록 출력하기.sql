SELECT  WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, COALESCE(FREEZER_YN, "N") AS "FREEZER_YN"
FROM    FOOD_WAREHOUSE
WHERE   SUBSTRING(WAREHOUSE_NAME, 4,2) = "경기"
ORDER   BY WAREHOUSE_ID ASC;