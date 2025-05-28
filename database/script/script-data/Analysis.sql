-- CRUD para la tabla Analysis

-- CREATE
INSERT INTO Analysis (id_analysis, input_image_path, timestamp, status, processing_time)
VALUES (1, 'training_data/CANGURO/img_001.jpg', GETDATE(), 'COMPLETADO', GETDATE());

-- READ
SELECT * FROM Analysis;
SELECT * FROM Analysis WHERE id_analysis = 1;

-- UPDATE
UPDATE Analysis
SET status = 'ERROR', processing_time = GETDATE()
WHERE id_analysis = 1;

-- DELETE
DELETE FROM Analysis WHERE id_analysis = 1;
