SELECT NAME
FROM (SELECT * 
      FROM ANIMAL_INS
      ORDER BY DATETIME)
WHERE ROWNUM = 1
-- https://programmers.co.kr/learn/courses/30/lessons/59405

/* 
상위 n개 출력 방법

1) ORACEL
   SELECT * FROM table WHERE ROWNUM <= n
2) MySQL
   SELECT * FROM table LIMIT n
3) SQL Server
   SELECT TOP n * FROM table
