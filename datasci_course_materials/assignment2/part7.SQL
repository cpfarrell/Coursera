SELECT element.value
FROM (
	SELECT a.row_num, b.col_num, SUM(a.value * b.value) as value
	FROM A a, B b
	WHERE a.col_num == b.row_num
	GROUP BY a.row_num, b.col_num
) element
WHERE element.row_num == 2 AND element.col_num == 3;