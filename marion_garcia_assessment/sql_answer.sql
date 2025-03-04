--Extracting quantity by age

SELECT c.customer_id, SUM(o.quantity) AS quantity_sum
FROM customer c left join sales s ON c.customer_id = s.customer_id
left join orders o ON s.sales_id = o.sales_id
left join items i on i.item_id = o.item_id
WHERE age BETWEEN 18 AND 35
GROUP BY c.customer_id

--Quantity by customer_id and item

SELECT c.customer_id, i.item_name, SUM(o.quantity) AS quantity_sum
FROM customer c left join sales s ON c.customer_id = s.customer_id
left join orders o ON s.sales_id = o.sales_id
left join items i on i.item_id = o.item_id
WHERE age BETWEEN 18 AND 35
GROUP BY c.customer_id, i.item_name