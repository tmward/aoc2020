/* To run: sqlite3 < solve.sql */
/* Load data into table expenses */
.headers on
.mode csv
CREATE TABLE expenses(expense INTEGER);
.import input.txt expenses

/* Calculate part 1 */
SELECT A.expense * B.expense as "Part 1 answer"
  FROM expenses AS A,
       expenses AS B
 WHERE A.expense + B.expense = 2020
 LIMIT 1;

/* Calculate part 2 */
SELECT A.expense * B.expense * C.expense as "Part 2 answer"
  FROM expenses AS A,
       expenses AS B,
       expenses AS C
 WHERE A.expense + B.expense + C.expense = 2020
 LIMIT 1;
