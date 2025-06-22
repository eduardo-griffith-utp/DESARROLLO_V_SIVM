-- CRUD para la tabla ItemTag

-- CREATE
-- Primero definimos las categorías generales (tags):
INSERT INTO Tag (tag_id, tag_name) VALUES
(1, 'animal'),
(2, 'mamífero'),
(3, 'marsupial'),
(4, 'monumento'),
(5, 'electrónico'),
(6, 'herramienta'),
(7, 'vehículo'),
(8, 'objeto cotidiano'),
(9, 'naturaleza'),
(10, 'fruta'),
(11, 'edificio'),
(12, 'acuático'),
(13, 'mamífero marino'),
(14, 'instrumento musical'),
(15, 'tecnología móvil'),
(16, 'ropa'),
(17, 'deportivo'),
(18, 'aparato doméstico'),
(19, 'paisaje natural');

-- Ahora insertamos los ItemTags con su respectiva categoría (tag_id):
INSERT INTO ItemTag (id_item_tag, tag_name, tag_id) VALUES
(1, 'CANGURO', 1),
(2, 'CRISTO REDENTOR', 4),
(3, 'DELFIN', 12),
(4, 'ELEFANTE', 1),
(5, 'ESTATUA DE LA LIBERTAD', 4),
(6, 'JIRAFA', 1),
(7, 'KOALA', 1),
(8, 'LAPTOP', 5),
(9, 'LIBRO', 8),
(10, 'LLAVE', 6),
(11, 'MOUSE', 5),
(12, 'OSO POLAR', 1),
(13, 'PARAGUA', 8),
(14, 'PEZ PAYASO', 12),
(15, 'PUENTE CENTENARIO', 11),
(16, 'RINOCERONTE', 1),
(17, 'ROD CAREW ESTADIO', 17),
(18, 'SMARTPHONE', 15),
(19, 'TORRE EIFFEL', 4),
(20, 'VOLCAN BARU', 9),
(21, 'BICICLETA', 7),
(22, 'CAMARA', 5),
(23, 'ZAPATILLA', 8),
(24, 'CAFETERA', 18),
(25, 'PIANO', 14),
(26, 'MARTILLO', 6),
(27, 'LAGO', 19),
(28, 'CAMISETA', 16),
(29, 'BANANA', 10),
(30, 'TELEVISOR', 5);

-- READ
SELECT * FROM ItemTag;
SELECT * FROM ItemTag WHERE id_tag = ?;

-- UPDATE
UPDATE ItemTag
SET tag_name = 'Colocar Nuevo'
WHERE id_tag = ?;

-- DELETE
DELETE FROM ItemTag WHERE id_tag = ?;
