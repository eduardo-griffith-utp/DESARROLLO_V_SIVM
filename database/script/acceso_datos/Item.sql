-- Obtener todos los ítems
SELECT * FROM Item;

-- Insertar un nuevo ítem
INSERT INTO Item (item_tag_id, name, description)
VALUES (1, 'Cámara de Seguridad', 'Dispositivo de vigilancia exterior');

-- Actualizar información del ítem
UPDATE Item
SET name = 'Cámara HD'
WHERE id_item = 1;

-- Eliminar un ítem
DELETE FROM Item
WHERE id_item = 1;
