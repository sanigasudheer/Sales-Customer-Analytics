-- ============================================
-- SALES & CUSTOMER ANALYTICS
-- SQL ANALYSIS
-- Database: sales_customer_analytics
-- Table: sales
-- ============================================

USE sales_customer_analytics;


-- ============================================
-- 1. OVERALL SALES AND PROFIT
-- ============================================

SELECT
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(sales) AS average_sales
FROM sales;


-- ============================================
-- 2. SALES BY CATEGORY
-- ============================================

SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY category
ORDER BY total_sales DESC;


-- ============================================
-- 3. SALES BY REGION
-- ============================================

SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY region
ORDER BY total_sales DESC;


-- ============================================
-- 4. YEARLY SALES AND PROFIT
-- ============================================

SELECT
    YEAR(order_date) AS year,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY YEAR(order_date)
ORDER BY year;


-- ============================================
-- 5. TOP 10 PRODUCTS BY SALES
-- ============================================

SELECT
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;


-- ============================================
-- 6. TOP 10 CUSTOMERS BY SALES
-- ============================================

SELECT
    customer_id,
    customer_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC
LIMIT 10;


-- ============================================
-- 7. DISCOUNT ANALYSIS
-- ============================================

SELECT
    discount,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY discount
ORDER BY discount;


-- ============================================
-- 8. SUB-CATEGORY PERFORMANCE
-- ============================================

SELECT
    sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin
FROM sales
GROUP BY sub_category
ORDER BY total_sales DESC;


-- ============================================
-- 9. AVERAGE ORDER VALUE (AOV)
-- ============================================

SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(
        SUM(sales) / COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM sales;


-- ============================================
-- 10. PROFITABILITY CLASSIFICATION
-- ============================================

SELECT
    order_id,
    product_name,
    sales,
    profit,
    CASE
        WHEN profit > 0 THEN 'Profitable'
        WHEN profit < 0 THEN 'Loss'
        ELSE 'No Profit'
    END AS profit_status
FROM sales;


-- ============================================
-- 11. TOP PROFITABLE SUB-CATEGORIES USING CTE
-- ============================================

WITH subcategory_profit AS (
    SELECT
        sub_category,
        SUM(sales) AS total_sales,
        SUM(profit) AS total_profit
    FROM sales
    GROUP BY sub_category
)

SELECT
    sub_category,
    ROUND(total_sales, 2) AS total_sales,
    ROUND(total_profit, 2) AS total_profit
FROM subcategory_profit
ORDER BY total_profit DESC;

-- ============================================
-- 12. RANKING SUB-CATEGORIES BY PROFIT
-- ============================================

WITH subcategory_profit AS (
    SELECT
        sub_category,
        SUM(sales) AS total_sales,
        SUM(profit) AS total_profit
    FROM sales
    GROUP BY sub_category
)

SELECT
    sub_category,
    ROUND(total_sales, 2) AS total_sales,
    ROUND(total_profit, 2) AS total_profit,
    RANK() OVER (ORDER BY total_profit DESC) AS profit_rank
FROM subcategory_profit
ORDER BY profit_rank;