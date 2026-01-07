# Write your MySQL query statement below

-- Find the ids of products that are both low fat and recyclable
SELECT product_id
FROM Products
WHERE Products.low_fats = 'Y' AND Products.recyclable = 'Y';