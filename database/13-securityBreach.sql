SELECT * FROM users WHERE attribute 
LIKE BINARY CONCAT('_%\%',first_name,'\_',second_name,'\%%')
ORDER BY attribute;