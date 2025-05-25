-- Obtener todos los resultados de análisis
SELECT * FROM AnalysisResult;

-- Insertar un nuevo análisis
INSERT INTO AnalysisResult (item_id, analysis_id, detected_labels, date_analysis, status)
VALUES (1, 2, 'Carro, Calle', NOW(), 'completo');

-- Actualizar etiquetas detectadas
UPDATE AnalysisResult
SET detected_labels = 'Persona, Calle'
WHERE id_analysis_result = 1;

-- Eliminar un análisis
DELETE FROM AnalysisResult
WHERE id_analysis_result = 1;
