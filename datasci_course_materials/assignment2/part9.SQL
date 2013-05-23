CREATE VIEW AddFrequency AS
SELECT *
FROM (
     SELECT * FROM frequency
     UNION
     SELECT 'q' as docid, 'washington' as term, 1 as count 
     UNION
     SELECT 'q' as docid, 'taxes' as term, 1 as count
     UNION 
     SELECT 'q' as docid, 'treasury' as term, 1 as count
);

SELECT matches.doc1, SUM(square) as score
FROM (
	SELECT x.docid as doc1, y.docid as doc2, x.count * y.count as square
	FROM Expanded x, Expanded y
	WHERE x.term == y.term AND y.docid = "q"
) matches
GROUP BY matches.doc1
ORDER BY score;