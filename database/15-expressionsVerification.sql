SELECT * FROM expressions 
WHERE(operation = '+' AND a + b = c) 
    OR(operation = '-' AND a - b = c)
    OR(operation = '*' AND a * b = c)
    OR(operation = '/' AND a / b = c);