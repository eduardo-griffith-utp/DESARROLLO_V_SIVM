-- CRUD para la tabla AnalysisResult

-- CREATE
INSERT INTO AnalysisResult (item_id, analysis_id, detected_labes, date_analysis, status)
VALUES 
(1, 1, 'canguro, marsupial, animal', '2025-06-20 10:00:00', 'VALIDO'),
(2, 1, 'cristo redentor, estatua, monumento', '2025-06-20 10:10:00', 'VALIDO'),
(3, 2, 'cubierto, utensilio, cocina', '2025-06-20 10:20:00', 'VALIDO'),
(4, 2, 'delfin, mamifero, acuatico', '2025-06-20 10:30:00', 'VALIDO'),
(5, 3, 'elefante, mamifero, grande', '2025-06-20 10:40:00', 'REVISADO'),
(6, 3, 'estatua de la libertad, monumento, usa', '2025-06-20 10:50:00', 'VALIDO'),
(7, 4, 'jirafa, cuello largo, animal', '2025-06-20 11:00:00', 'VALIDO'),
(8, 4, 'koala, marsupial, animal', '2025-06-20 11:10:00', 'PENDIENTE'),
(9, 5, 'laptop, computadora, electronica', '2025-06-20 11:20:00', 'VALIDO'),
(10, 5, 'lentes, accesorio, vision', '2025-06-20 11:30:00', 'VALIDO'),
(11, 6, 'leon, felino, salvaje', '2025-06-20 11:40:00', 'VALIDO'),
(12, 6, 'libro, lectura, papel', '2025-06-20 11:50:00', 'REVISADO'),
(13, 7, 'llave, metal, herramienta', '2025-06-20 12:00:00', 'VALIDO'),
(14, 7, 'mouse, periferico, computadora', '2025-06-20 12:10:00', 'VALIDO'),
(15, 8, 'oso polar, mamifero, arctico', '2025-06-20 12:20:00', 'PENDIENTE'),
(16, 8, 'panda, mamifero, oso', '2025-06-20 12:30:00', 'VALIDO'),
(17, 9, 'paragua, lluvia, accesorio', '2025-06-20 12:40:00', 'VALIDO'),
(18, 9, 'pez payaso, acuario, pez', '2025-06-20 12:50:00', 'REVISADO'),
(19, 10, 'puente centenario, infraestructura, panama', '2025-06-20 13:00:00', 'VALIDO'),
(20, 10, 'rinoceronte, mamifero, salvaje', '2025-06-20 13:10:00', 'VALIDO'),
(21, 11, 'rod carew estadio, deporte, beisbol', '2025-06-20 13:20:00', 'VALIDO'),
(22, 11, 'smartphone, telefono, electronica', '2025-06-20 13:30:00', 'PENDIENTE'),
(23, 12, 'taza, bebida, ceramica', '2025-06-20 13:40:00', 'VALIDO'),
(24, 12, 'tigre, felino, salvaje', '2025-06-20 13:50:00', 'REVISADO'),
(25, 13, 'torre eiffel, monumento, paris', '2025-06-20 14:00:00', 'VALIDO'),
(26, 13, 'ventilador, electrodomestico, aire', '2025-06-20 14:10:00', 'VALIDO'),
(27, 14, 'volcan baru, naturaleza, panama', '2025-06-20 14:20:00', 'PENDIENTE'),
(28, 14, 'bicicleta, transporte, deporte', '2025-06-20 14:30:00', 'VALIDO'),
(29, 15, 'camara, fotografia, electronica', '2025-06-20 14:40:00', 'VALIDO'),
(30, 15, 'zapatilla, calzado, deporte', '2025-06-20 14:50:00', 'VALIDO');


-- READ
SELECT * FROM AnalysisResult;
SELECT * FROM AnalysisResult WHERE id_analysis_result = 1;

-- UPDATE
UPDATE AnalysisResult
SET detected_labes = 'canguro, animal', status = 'REVISADO'
WHERE id_analysis_result = 1;

-- DELETE
DELETE FROM AnalysisResult WHERE id_analysis_result = 1;
