-- CRUD para la tabla MediaContent

-- CREATE
INSERT INTO MediaContent (item_id, route_path, type, description, date_uploaded)
VALUES
(1, 'assets/storage_structure/training_data/CANGURO/Canguro-1.jpg', 'image', 'CANGURO - Canguro-1.jpg', '2025-06-16 16:23:58'),
(1, 'assets/storage_structure/training_data/CANGURO/Canguro-2.jpg', 'image', 'CANGURO - Canguro-2.jpg', '2025-06-16 16:23:58'),
(1, 'assets/storage_structure/training_data/CANGURO/Canguro-3.jpg', 'image', 'CANGURO - Canguro-3.jpg', '2025-06-16 16:23:58'),
(1, 'assets/storage_structure/training_data/CANGURO/Canguro-4.jpg', 'image', 'CANGURO - Canguro-4.jpg', '2025-06-16 16:23:58'),
(1, 'assets/storage_structure/training_data/CANGURO/Canguro-5.jpg', 'image', 'CANGURO - Canguro-5.jpg', '2025-06-16 16:23:58');
(2, 'assets/storage_structure/training_data/CRISTO REDENTOR/Cristo-Redentor-1.jpg', 'image', 'CRISTO REDENTOR - Cristo-Redentor-1.jpg', '2025-06-16 16:23:58'),
(2, 'assets/storage_structure/training_data/CRISTO REDENTOR/Cristo-Redentor-2.jpg', 'image', 'CRISTO REDENTOR - Cristo-Redentor-2.jpg', '2025-06-16 16:23:58'),
(2, 'assets/storage_structure/training_data/CRISTO REDENTOR/Cristo-Redentor-3.jpg', 'image', 'CRISTO REDENTOR - Cristo-Redentor-3.jpg', '2025-06-16 16:23:58'),
(2, 'assets/storage_structure/training_data/CRISTO REDENTOR/Cristo-Redentor-4.jpg', 'image', 'CRISTO REDENTOR - Cristo-Redentor-4.jpg', '2025-06-16 16:23:58');

-- READ
SELECT * FROM MediaContent;
SELECT * FROM MediaContent WHERE id_media_content = 1;

-- UPDATE
UPDATE MediaContent
SET route_path = 'nuevo_path.jpg', description = 'Actualización'
WHERE id_media_content = 1;

-- DELETE
DELETE FROM MediaContent WHERE id_media_content = 1;
