-- CRUD para la tabla ItemTag

-- CREATE
INSERT INTO ItemTag (tag_name)
VALUES 
('CANGURO'),
('CRISTO RENDENTOR'),
('CUBIERTO'),
('DELFIN'),
('ELEFANTE'),
('ESTATUA DE LA LIBERTAD'),
('JIRAFA'),
('KOALA'),
('LAPTOP'),
('LENTES'),
('LEON'),
('LIBRO'),
('LLAVE'),
('MOUSE'),
('OSO POLAR'),
('PANDA'),
('PARAGUA'),
('PEZ PAYASO'),
('PUENTE CENTENARIO'),
('RINOCERONTE'),
('ROD CAREW ESTADIO'),
('SMARTPHONE'),
('TAZA'),
('TIGRE'),
('TORRE EIFFEL'),
('VENTILADOR'),
('VOLCAN BARU');

-- READ
SELECT * FROM ItemTag;
SELECT * FROM ItemTag WHERE id_tag = ?;

-- UPDATE
UPDATE ItemTag
SET tag_name = 'Colocar Nuevo'
WHERE id_tag = ?;

-- DELETE
DELETE FROM ItemTag WHERE id_tag = ?;
