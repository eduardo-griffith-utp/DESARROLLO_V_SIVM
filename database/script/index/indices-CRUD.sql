-- Buscar todos los ítems que pertenezcan a una categoría específica
SELECT id_item, name, description
FROM Item
WHERE item_tag_id = 3;

-- Buscar ítems relacionados con la palabra "cámara"
SELECT id_item, name, description
FROM Item
WHERE MATCH(name, description) AGAINST ('+cámara' IN BOOLEAN MODE);

-- Actualizar el estado de análisis antiguos
UPDATE AnalysisResult
SET status = 'archivado'
WHERE date_analysis < '2023-01-01' AND status = 'procesado';

-- Eliminar contenido multimedia asociado a un ítem eliminado
DELETE FROM MediaContent
WHERE item_id = 10;

-- Obtener los nombres de ítems y sus etiquetas detectadas
SELECT i.name, ar.detected_labels, ar.date_analysis
FROM AnalysisResult ar
JOIN Item i ON ar.item_id = i.id_item
WHERE ar.status = 'completo';

-- Buscar análisis que contienen la palabra "persona" en los resultados
SELECT ar.detected_labels, a.timestamp, a.source
FROM AnalysisResult ar
JOIN Analysis a ON ar.analysis_id = a.id_analysis
WHERE MATCH(ar.detected_labels) AGAINST ('persona');