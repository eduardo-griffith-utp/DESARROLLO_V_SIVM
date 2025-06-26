-- CRUD para la tabla Analysis

-- CREATE
INSERT INTO Analysis (input_image_path, timestamp, status, processing_time)
VALUES
('training_data/CANGURO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/CRISTO-RENDENTOR/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/CUBIERTO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/DELFIN/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/ELEFANTE/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/ESTATUA-DE-LA-LIBERTAD/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/JIRAFA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/KOALA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/LAPTOP/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/LENTES/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/LEON/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/LIBRO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/LLAVE/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/MOUSE/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/OSO-POLAR/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/PANDA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/PARAGUA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/PEZ-PAYASO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/PUENTE-CENTENARIO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/RINOCERONTE/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/ROD-CAREW-ESTADIO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/SMARTPHONE/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/TAZA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/TIGRE/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/TORRE-EIFFEL/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/VENTILADOR/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/VOLCAN-BARU/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/BICICLETA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/CAMARA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/ZAPATILLA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/CAFETERA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/PIANO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/MARTILLO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/LAGO/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/CAMISETA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/BANANA/img_001.jpg', NOW(), 'COMPLETADO', NOW()),
('training_data/TELEVISOR/img_001.jpg', NOW(), 'COMPLETADO', NOW());

-- READ
SELECT * FROM Analysis;
SELECT * FROM Analysis WHERE id_analysis = 1;

/*
-- UPDATE
UPDATE Analysis
SET status = 'ERROR', processing_time = NOW()
WHERE id_analysis = 1;

-- DELETE
DELETE FROM Analysis WHERE id_analysis = 1;
/*