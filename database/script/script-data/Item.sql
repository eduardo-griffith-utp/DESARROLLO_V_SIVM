-- CRUD para la tabla Item

-- CREATE
INSERT INTO Item (item_tag_id, name, description)
VALUES 
(1, 'CANGURO', 'Mamífero marsupial conocido por sus grandes saltos.'),
(2, 'CRISTO REDENTOR', 'Famosa estatua en Río de Janeiro, Brasil.'),
(3, 'DELFIN', 'Inteligente mamífero marino de comportamiento amigable.'),
(4, 'ELEFANTE', 'El animal terrestre más grande del planeta.'),
(5, 'ESTATUA DE LA LIBERTAD', 'Símbolo icónico de libertad en Nueva York.'),
(6, 'JIRAFA', 'Mamífero de cuello largo que vive en África.'),
(7, 'KOALA', 'Animal australiano que duerme hasta 20 horas al día.'),
(8, 'LAPTOP', 'Computadora portátil de uso personal o profesional.'),
(9, 'LIBRO', 'Objeto usado para leer y almacenar información.'),
(10, 'LLAVE', 'Herramienta para abrir cerraduras o candados.'),
(11, 'MOUSE', 'Dispositivo que permite interactuar con la computadora.'),
(12, 'OSO POLAR', 'Gran depredador ártico adaptado al frío extremo.'),
(13, 'PARAGUA', 'Objeto que protege de la lluvia.'),
(14, 'PEZ PAYASO', 'Pez colorido popularizado por películas animadas.'),
(15, 'PUENTE CENTENARIO', 'Puente emblemático ubicado en Panamá.'),
(16, 'RINOCERONTE', 'Animal robusto con uno o dos cuernos en la cabeza.'),
(17, 'ROD CAREW ESTADIO', 'Estadio de béisbol importante en Panamá.'),
(18, 'SMARTPHONE', 'Teléfono inteligente con múltiples funciones.'),
(19, 'TORRE EIFFEL', 'Famosa torre de hierro ubicada en París.'),
(20, 'VOLCAN BARU', 'El punto más alto de Panamá.'),
(21, 'BICICLETA', 'Medio de transporte ecológico de dos ruedas.'),
(22, 'CAMARA', 'Dispositivo para capturar fotografías o video.'),
(23, 'ZAPATILLA', 'Calzado cómodo usado para caminar o hacer deporte.'),
(24, 'CAFETERA', 'Dispositivo usado para preparar café.'),
(25, 'PIANO', 'Instrumento musical de cuerdas y teclas.'),
(26, 'MARTILLO', 'Herramienta usada para clavar o golpear objetos.'),
(27, 'LAGO', 'Cuerpo de agua dulce rodeado de tierra.'),
(28, 'CAMISETA', 'Prenda de vestir casual para el torso.'),
(29, 'BANANA', 'Fruta tropical amarilla y rica en potasio.'),
(30, 'TELEVISOR', 'Dispositivo para ver programas y películas.');

-- READ
SELECT * FROM Item;
SELECT * FROM Item WHERE id_item = ?;

-- UPDATE
UPDATE Item
SET name = 'Imagen modificada', description = 'Descripción nueva'
WHERE id_item = ?;

-- DELETE
DELETE FROM Item WHERE id_item = ?;
