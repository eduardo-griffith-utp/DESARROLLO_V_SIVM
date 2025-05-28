-- CRUD para la tabla AnalysisResult

-- CREATE
INSERT INTO AnalysisResult (id_analysis_result, item_id, analysis_id, detected_labes, date_analysis, status)
VALUES (1, 1, 1, 'canguro', GETDATE(), 'VALIDO');

-- READ
SELECT * FROM AnalysisResult;
SELECT * FROM AnalysisResult WHERE id_analysis_result = 1;

-- UPDATE
UPDATE AnalysisResult
SET detected_labes = 'canguro, animal', status = 'REVISADO'
WHERE id_analysis_result = 1;

-- DELETE
DELETE FROM AnalysisResult WHERE id_analysis_result = 1;
