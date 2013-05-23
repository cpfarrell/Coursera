SELECT count(*)
FROM (
	SELECT DISTINCT x.docid
	FROM Frequency x
	GROUP BY x.docid
	HAVING sum(x.count)>300
) x;