-- CRUD para la tabla MediaContent

-- CREATE
INSERT INTO MediaContent (item_id, route_path, type, description, date_uploaded)
VALUES (1, 'training_data/CANGURO/img_001.jpg', 'image/jpeg', 'Imagen de canguro', GETDATE());

-- READ
SELECT * FROM MediaContent;
SELECT * FROM MediaContent WHERE id_media_content = 1;

-- UPDATE
UPDATE MediaContent
SET route_path = 'nuevo_path.jpg', description = 'Actualización'
WHERE id_media_content = 1;

-- DELETE
DELETE FROM MediaContent WHERE id_media_content = 1;
