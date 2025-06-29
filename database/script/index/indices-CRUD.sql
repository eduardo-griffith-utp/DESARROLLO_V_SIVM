-- Buscar todos los ítems que pertenezcan a una categoría específica
-- Usa: idx_item_tag_id
SELECT id_item, name, description
FROM Item
WHERE item_tag_id = 3;

-- Buscar ítems por coincidencia exacta en el nombre
-- Usa: ft_item_name
SELECT id_item, name, description
FROM Item
WHERE MATCH(name) AGAINST ('cámara');

-- Buscar ítems por coincidencia exacta en la descripción
-- Usa: ft_item_description
SELECT id_item, name, description
FROM Item
WHERE MATCH(description) AGAINST ('profesional');

-- Buscar un tag específico por nombre
-- Usa: idx_tag_name
SELECT * FROM ItemTag
WHERE tag_name = 'Electrónica';

-- Buscar contenido multimedia por fecha de subida
-- Usa: idx_media_date_uploaded
SELECT * FROM MediaContent
WHERE date_uploaded > '2024-01-01';

-- Buscar contenido multimedia por tipo
-- Usa: idx_media_type
SELECT * FROM MediaContent
WHERE type = 'imagen';

-- Buscar análisis por rango de fecha/hora
-- Usa: idx_analysis_timestamp
SELECT * FROM Analysis
WHERE timestamp BETWEEN '2024-01-01' AND '2024-12-31';

-- Buscar análisis por coincidencia en la ruta de imagen
-- Usa: ft_analysis_input_image_path
SELECT * FROM Analysis
WHERE MATCH(input_image_path) AGAINST ('foto123');

-- Buscar resultados de análisis por ítem específico
-- Usa: idx_result_item_id
SELECT * FROM AnalysisResult
WHERE item_id = 20;

-- Buscar resultados de análisis por análisis específico
-- Usa: idx_result_analysis_id
SELECT * FROM AnalysisResult
WHERE analysis_id = 100;

-- Buscar resultados de análisis por fecha
-- Usa: idx_result_date_analysis
SELECT * FROM AnalysisResult
WHERE date_analysis = '2024-06-10';

-- Buscar resultados de análisis por estado
-- Usa: idx_result_status
SELECT * FROM AnalysisResult
WHERE status = 'COMPLETED';

-- Buscar resultados de análisis por coincidencia en etiquetas detectadas
-- Usa: ft_detected_labels
SELECT * FROM AnalysisResult
WHERE MATCH(detected_labels) AGAINST ('persona');

-- =========================
-- ESCENARIOS DE ACTUALIZACIÓN
-- =========================

-- Actualizar la descripción de un ítem por su id
-- Usa: PRIMARY KEY o índice único en id_item
UPDATE Item
SET description = 'Nueva descripción'
WHERE id_item = 5;

-- Actualizar el nombre de un tag específico
-- Usa: idx_tag_name
UPDATE ItemTag
SET tag_name = 'Tecnología'
WHERE tag_name = 'Electrónica';

-- Actualizar el tipo de contenido multimedia por su id
-- Usa: PRIMARY KEY o índice único en id_media_content
UPDATE MediaContent
SET type = 'video'
WHERE id_media_content = 12;

-- Actualizar el estado de un análisis por su id
-- Usa: PRIMARY KEY o índice único en id_analysis
UPDATE Analysis
SET status = 'FINALIZADO'
WHERE id_analysis = 8;

-- Actualizar el estado de resultados de análisis por fecha
-- Usa: idx_result_date_analysis
UPDATE AnalysisResult
SET status = 'ARCHIVADO'
WHERE date_analysis < '2024-01-01';

-- Actualizar etiquetas detectadas en resultados de un ítem específico
-- Usa: idx_result_item_id
UPDATE AnalysisResult
SET detected_labels = 'vehículo, persona'
WHERE item_id = 20;