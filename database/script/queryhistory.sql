-- desarrollov_app.queryhistory definition

CREATE TABLE `queryhistory` (
  `id_querys` int(11) NOT NULL,
  `imagen_id` int(11) NOT NULL,
  `date_consultation` datetime NOT NULL,
  `counter` int(11) NOT NULL,
  PRIMARY KEY (`id_querys`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;