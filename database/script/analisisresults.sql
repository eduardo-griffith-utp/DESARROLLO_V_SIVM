-- desarrollov_app.analisisresults definition

CREATE TABLE `analisisresults` (
  `id_results` int(11) NOT NULL,
  `imagen_id` int(11) NOT NULL,
  `detected_labels` varchar(50) NOT NULL,
  `date_analisys` datetime NOT NULL,
  PRIMARY KEY (`id_results`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;