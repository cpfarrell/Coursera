SELECT count(*)
FROM (
	SELECT DISTINCT x.docid
	FROM Frequency x
	WHERE x.term="parliament" AND x.count>0
) x;