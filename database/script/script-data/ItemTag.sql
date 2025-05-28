-- CRUD para la tabla ItemTag

-- CREATE
INSERT INTO ItemTag (id_tag, tag_name)
VALUES 
(1, 'CANGURO'),
(2, 'CRISTO RENDENTOR'),
(3, 'CUBIERTO'),
(4, 'DELFIN'),
(5, 'ELEFANTE'),
(6, 'ESTATUA DE LA LIBERTAD'),
(7, 'JIRAFA'),
(8, 'KOALA'),
(9, 'LAPTOP'),
(10, 'LENTES'),
(11, 'LEON'),
(12, 'LIBRO'),
(13, 'LLAVE'),
(14, 'MOUSE'),
(15, 'OSO POLAR'),
(16, 'PANDA'),
(17, 'PARAGUA'),
(18, 'PEZ PAYASO'),
(19, 'PUENTE CENTENARIO'),
(20, 'RINOCERONTE'),
(21, 'ROD CAREW ESTADIO'),
(22, 'SMARTPHONE'),
(23, 'TAZA'),
(24, 'TIGRE'),
(25, 'TORRE EIFFEL'),
(26, 'VENTILADOR'),
(27, 'VOLCAN BARU');

-- READ
SELECT * FROM ItemTag;
SELECT * FROM ItemTag WHERE id_tag = ?;

-- UPDATE
UPDATE ItemTag
SET tag_name = 'Colocar Nuevo'
WHERE id_tag = ?;

-- DELETE
DELETE FROM ItemTag WHERE id_tag = ?;
