-- desarrollov_app.images definition

CREATE TABLE `images` (
  `id_imagen` int(11) NOT NULL AUTO_INCREMENT,
  `route_imagen` varchar(50) NOT NULL,
  `date_uploaded` varchar(50) NOT NULL,
  PRIMARY KEY (`id_imagen`),
  CONSTRAINT `images_analisisresults_FK` FOREIGN KEY (`id_imagen`) REFERENCES `analisisresults` (`id_results`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `images_multimedia_FK` FOREIGN KEY (`id_imagen`) REFERENCES `multimedia` (`id_multimedia`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `images_queryhistory_FK` FOREIGN KEY (`id_imagen`) REFERENCES `queryhistory` (`id_querys`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;