# Write your MySQL query statement below

SELECT e_uni.unique_id, e.name
FROM Employees e

/*
We want to keep all employees
    -> Suggests LEFT JOIN
REGARDLESS of whether we are able to find a unique id for them
    -> Eliminates INNER JOIN
*/
LEFT JOIN EmployeeUNI e_uni
ON e.id = e_uni.id;