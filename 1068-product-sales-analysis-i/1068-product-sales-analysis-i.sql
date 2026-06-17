SELECT Product.product_name, sale.year, sale.price
FROM Sales AS sale
LEFT JOIN Product ON sale.product_id = product.product_id