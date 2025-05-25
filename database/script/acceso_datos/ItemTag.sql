-- Ver todas las etiquetas
SELECT * FROM ItemTag;

-- Insertar nueva etiqueta
INSERT INTO ItemTag (tag_name)
VALUES ('Electrónica');

-- Actualizar etiqueta
UPDATE ItemTag
SET tag_name = 'Tecnología'
WHERE id_tag = 1;

-- Eliminar una etiqueta
DELETE FROM ItemTag
WHERE id_tag = 1;
