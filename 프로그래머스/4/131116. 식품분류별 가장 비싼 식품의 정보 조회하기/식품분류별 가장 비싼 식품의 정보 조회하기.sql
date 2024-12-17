-- 코드를 입력하세요
SELECT 
    CATEGORY, 
    PRICE AS MAX_PRICE,
    PRODUCT_NAME
FROM FOOD_PRODUCT 
WHERE (PRICE, CATEGORY) IN (
        SELECT 
            MAX(PRICE),
            CATEGORY
        FROM FOOD_PRODUCT
        GROUP BY CATEGORY
        HAVING CATEGORY IN ("과자", "국", "김치", "식용유")
        )
ORDER BY 2 DESC