SELECT ANIMAL_ID, NAME, 
    CASE
    WHEN SEX_UPON_INTAKE LIKE 'intact%' THEN 'X'
    ELSE 'O'
    END AS 중성화
FROM ANIMAL_INS