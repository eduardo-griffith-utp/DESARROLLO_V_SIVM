-- =========================
-- ESCENARIOS DE CONSULTAS CON JOIN ENTRE DOS TABLAS USANDO ÍNDICES
-- =========================

-- Obtener todos los ítems y el nombre de su categoría/tag
-- Usa: idx_item_tag_id en Item y PRIMARY KEY en ItemTag
SELECT i.id_item, i.name, t.tag_name
FROM Item i
JOIN ItemTag t ON i.item_tag_id = t.id_tag;

-- Buscar ítems que pertenezcan a la categoría 'Electrónica'
-- Usa: idx_tag_name en ItemTag y idx_item_tag_id en Item
SELECT i.id_item, i.name, i.description
FROM Item i
JOIN ItemTag t ON i.item_tag_id = t.id_tag
WHERE t.tag_name = 'Electrónica';

-- Obtener el contenido multimedia de los ítems de una categoría específica
-- Usa: idx_item_tag_id en Item, idx_media_item_id en MediaContent
SELECT m.*
FROM MediaContent m
JOIN Item i ON m.item_id = i.id_item
WHERE i.item_tag_id = 2;

-- Buscar resultados de análisis y el nombre del ítem asociado
-- Usa: idx_result_item_id en AnalysisResult, PRIMARY KEY en Item
SELECT ar.*, i.name
FROM AnalysisResult ar
JOIN Item i ON ar.item_id = i.id_item
WHERE ar.status = 'COMPLETED';

-- Obtener análisis y su resultado para un ítem específico
-- Usa: idx_result_item_id en AnalysisResult, PRIMARY KEY en Analysis
SELECT a.*, ar.detected_labels
FROM Analysis a
JOIN AnalysisResult ar ON a.id_analysis = ar.analysis_id
WHERE ar.item_id = 10;

-- Buscar todos los análisis realizados para ítems de la categoría 'Fotografía'
-- Usa: idx_item_tag_id en Item, idx_result_item_id en AnalysisResult, idx_tag_name en ItemTag
SELECT ar.*, i.name, t.tag_name
FROM AnalysisResult ar
JOIN Item i ON ar.item_id = i.id_item
JOIN ItemTag t ON i.item_tag_id = t.id_tag
WHERE t.tag_name = 'Fotografía';

-- Obtener el contenido multimedia y el nombre del ítem para archivos subidos después de cierta fecha
-- Usa: idx_media_date_uploaded en MediaContent, PRIMARY KEY en Item
SELECT m.route_path, m.type, i.name
FROM MediaContent m
JOIN Item i ON m.item_id = i.id_item
WHERE m.date_uploaded > '2024-01-01';