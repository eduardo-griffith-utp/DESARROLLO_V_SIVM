-- CRUD para la tabla Item

-- CREATE
INSERT INTO Item (item_tag_id, name, description)
VALUES 
(1, 'CANGURO', 'Fotografía de un canguro'),
(2, 'CRISTO REDENTOR', 'Fotografía del famoso monumento en Río de Janeiro'),
(3, 'CUBIERTO', 'Fotografía de un juego de cubiertos de plata'),
(4, 'DELFIN', 'Foto de un delfín saltando en el océano'),
(5, 'ELEFANTE', 'Fotografía de un elefante africano en la sabana'),
(6, 'ESTATUA DE LA LIBERTAD', 'Foto del emblemático monumento en Nueva York'),
(7, 'JIRAFA', 'Fotografía de una jirafa comiendo hojas de árbol'),
(8, 'KOALA', 'Foto de un koala abrazado a un árbol de eucalipto'),
(9, 'LAPTOP', 'Fotografía de una laptop moderna sobre escritorio'),
(10, 'LENTES', 'Foto de unos lentes de sol sobre mesa'),
(11, 'LEON', 'Fotografía de un león en el Serengeti'),
(12, 'LIBRO', 'Foto de un libro abierto sobre mesa de madera'),
(13, 'LLAVE', 'Fotografía de una llave antigua'),
(14, 'MOUSE', 'Foto de un mouse inalámbrico sobre pad'),
(15, 'OSO POLAR', 'Fotografía de un oso polar en el Ártico'),
(16, 'PANDA', 'Foto de un panda comiendo bambú'),
(17, 'PARAGUA', 'Fotografía de un paraguas abierto bajo la lluvia'),
(18, 'PEZ PAYASO', 'Foto de un pez payaso entre anémonas'),
(19, 'PUENTE CENTENARIO', 'Fotografía del puente sobre el Canal de Panamá'),
(20, 'RINOCERONTE', 'Foto de un rinoceronte en la sabana africana'),
(21, 'ROD CAREW ESTADIO', 'Fotografía del estadio de béisbol en Panamá'),
(22, 'SMARTPHONE', 'Foto de un smartphone último modelo'),
(23, 'TAZA', 'Fotografía de una taza de café humeante'),
(24, 'TIGRE', 'Foto de un tigre de bengala en la jungla'),
(25, 'TORRE EIFFEL', 'Fotografía del icónico monumento parisino'),
(26, 'VENTILADOR', 'Foto de un ventilador de techo moderno'),
(27, 'VOLCAN BARU', 'Fotografía del volcán más alto de Panamá');

-- READ
SELECT * FROM Item;
SELECT * FROM Item WHERE id_item = ?;

-- UPDATE
UPDATE Item
SET name = 'Imagen modificada', description = 'Descripción nueva'
WHERE id_item = ?;

-- DELETE
DELETE FROM Item WHERE id_item = ?;
