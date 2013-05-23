SELECT count(*)
FROM (
	SELECT x.term
	FROM Frequency x
	WHERE x.docid="10398_txt_earn" AND x.count==1
	UNION
        SELECT y.term
        FROM Frequency y
        WHERE y.docid="925_txt_trade" AND y.count==1
) x;