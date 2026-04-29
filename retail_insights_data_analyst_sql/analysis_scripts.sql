-- =========================================
-- 4. EXPIRING SOON PRODUCTS
-- =========================================
-- Expiring in next 7 days AND stock > 50

SELECT *
FROM Products
WHERE
    expiry_date <= SYSDATE + 7
    AND stock_count > 50;

-- =========================================
-- 5. DEAD STOCK ANALYSIS
-- =========================================
-- Products NOT sold in last 60 days

SELECT p.*
FROM
    Products p
    LEFT JOIN SalesTransactions s ON p.product_id = s.product_id
    AND s.sale_date >= SYSDATE - 60
WHERE
    s.product_id IS NULL;

-- =========================================
-- 6. REVENUE CONTRIBUTION
-- =========================================
-- Category revenue (last 30 days)

SELECT c.category_name, SUM(s.amount) AS total_revenue
FROM
    SalesTransactions s
    JOIN Products p ON s.product_id = p.product_id
    JOIN Categories c ON p.category_id = c.category_id
WHERE
    s.sale_date >= SYSDATE - 30
GROUP BY
    c.category_name
ORDER BY total_revenue DESC;