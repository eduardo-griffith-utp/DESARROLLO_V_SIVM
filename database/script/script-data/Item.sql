-- CRUD para la tabla Item

-- CREATE
INSERT INTO Item (id_item, item_tag_id, name, description)
VALUES (1, 1, 'Imagen de canguro', 'Imagen de entrenamiento');

-- READ
SELECT * FROM Item;
SELECT * FROM Item WHERE id_item = 1;

-- UPDATE
UPDATE Item
SET name = 'Imagen modificada', description = 'Descripción nueva'
WHERE id_item = 1;

-- DELETE
DELETE FROM Item WHERE id_item = 1;
