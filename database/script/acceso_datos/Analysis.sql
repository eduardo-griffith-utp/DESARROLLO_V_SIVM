-- Ver todos los análisis
SELECT * FROM Analysis;

-- Insertar un nuevo análisis
INSERT INTO Analysis (imput_image_path, timestamp, status, processing_time, source)
VALUES ('/images/input.jpg', NOW(), 'pendiente', NOW(), 'drone');

-- Cambiar estado de un análisis
UPDATE Analysis
SET status = 'completo'
WHERE id_analysis = 1;

-- Eliminar un análisis
DELETE FROM Analysis
WHERE id_analysis = 1;
