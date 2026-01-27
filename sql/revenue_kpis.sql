SELECT
    store_id,
    SUM(revenue) AS total_revenue_kpi,
    AVG(revenue) AS avg_order_value_kpi
FROM sales
GROUP BY store_id;