SELECT
    visit.customer_id,
    COUNT(visit.visit_id) AS count_no_trans
FROM Visits AS visit
    LEFT JOIN Transactions AS transaction
    ON transaction.visit_id = visit.visit_id
WHERE transaction.visit_id IS NULL
GROUP BY visit.customer_id