-- Obtener todos los registros
SELECT * FROM MediaContent;

-- Insertar un nuevo registro
INSERT INTO MediaContent (item_id, route_path, type, description, date_uploaded)
VALUES (1, '/images/item1.jpg', 'image', 'Imagen del ítem 1', NOW());

-- Actualizar un registro
UPDATE MediaContent
SET description = 'Imagen actualizada del ítem 1'
WHERE id_media_content = 1;

-- Eliminar un registro
DELETE FROM MediaContent
WHERE id_media_content = 1;
