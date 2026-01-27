SELECT
    store_id,
    COUNT(CASE WHEN inventory_on_hand = 0 THEN 1 END) * 1.0 / COUNT(*) AS stockout_rate_kpi
FROM inventory
GROUP BY store_id;