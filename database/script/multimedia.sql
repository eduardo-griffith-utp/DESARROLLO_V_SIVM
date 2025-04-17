-- desarrollov_app.multimedia definition

CREATE TABLE `multimedia` (
  `id_multimedia` int(11) NOT NULL,
  `imagen_id` int(11) NOT NULL,
  `type_content` varchar(30) NOT NULL,
  `description` varchar(50) NOT NULL,
  `file_path` varchar(64) NOT NULL,
  PRIMARY KEY (`id_multimedia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;