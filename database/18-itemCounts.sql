SELECT item_name,item_type,COUNT(*) AS item_count 
FROM availableItems 
GROUP BY item_name, item_type 
ORDER BY item_type,item_name;