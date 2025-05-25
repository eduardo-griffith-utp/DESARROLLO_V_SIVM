-- Insertar los ítems asociándolos a los tags correspondientes
INSERT INTO Item (item_tag_id, name, description) VALUES
-- Animales
(1, 'Canguro', 'Marsupial originario de Australia'),
(1, 'Delfin', 'Mamífero acuático inteligente'),
(1, 'Elefante', 'El mayor animal terrestre'),
(1, 'Jirafa', 'Animal con el cuello más largo'),
(1, 'Koala', 'Marsupial que vive en los eucaliptos'),
(1, 'León', 'El rey de la selva'),
(1, 'Oso polar', 'Gran oso blanco del Ártico'),
(1, 'Panda', 'Oso blanco y negro de China'),
(1, 'Pez payaso', 'Pez colorido que vive con anémonas'),
(1, 'Rinoceronte', 'Gran mamífero con cuerno'),
(1, 'Tigre', 'Gran felino rayado'),

-- Monumentos
(2, 'Cristo redentor', 'Estatua de Jesús en Río de Janeiro'),
(2, 'Estatua de la libertad', 'Icono de Nueva York'),
(2, 'Puente centenario', 'Puente en Panamá'),
(2, 'Rod carew estadio', 'Estadio de béisbol en Panamá'),
(2, 'Torre eifel', 'Torre icónica de París'),
(2, 'Volcan baru', 'Volcán inactivo en Panamá'),

-- Objetos cotidianos
(3, 'Cubierto', 'Utensilios para comer'),
(3, 'Lentes', 'Accesorio para mejorar la visión'),
(3, 'Libro', 'Fuente de conocimiento y entretenimiento'),
(3, 'Llave', 'Herramienta para abrir cerraduras'),
(3, 'Paragua', 'Protección contra la lluvia'),
(3, 'Taza', 'Recipiente para beber líquidos'),

-- Electrónicos
(4, 'Laptop', 'Computadora portátil'),
(4, 'Mouse', 'Dispositivo para interactuar con computadoras'),
(4, 'Smartphone', 'Teléfono inteligente'),
(4, 'Ventilador', 'Dispositivo para mover aire'),

-- Deporte (solo el estadio en este caso)
(5, 'Rod carew estadio', 'Estadio de béisbol en Panamá');