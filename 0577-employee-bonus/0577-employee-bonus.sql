# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e

/*
We want every employee regardless of whether they got a bonus or not
If we used INNER JOIN, employees without a bonus would not appear
*/
LEFT JOIN Bonus b
ON e.empID = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;