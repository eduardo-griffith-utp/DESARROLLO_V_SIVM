-- CRUD para la tabla ItemTag

-- CREATE
INSERT INTO ItemTag (id_tag, tag_name)
VALUES (1, 'CANGURO');

-- READ
SELECT * FROM ItemTag;
SELECT * FROM ItemTag WHERE id_tag = 1;

-- UPDATE
UPDATE ItemTag
SET tag_name = 'CANGURO ACTUALIZADO'
WHERE id_tag = 1;

-- DELETE
DELETE FROM ItemTag WHERE id_tag = 1;
