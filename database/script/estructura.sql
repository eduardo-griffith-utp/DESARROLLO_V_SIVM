

-- Tabla MediaContent
CREATE TABLE IF NOT EXISTS MediaContent(
    id_media_content INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    item_id INT NOT NULL,
    route_path VARCHAR(255) NOT NULL,
    type VARCHAR(30) NOT NULL,
    description VARCHAR(50),
    date_uploaded DATETIME NOT NULL
);

-- Tabla AnalysisResult
CREATE TABLE IF NOT EXISTS AnalysisResult(
    id_analysis_result INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    item_id INT NOT NULL,
    analisys_id int NOT NULL,
    detected_labels VARCHAR(50) NOT NULL,
    date_analysis DATETIME NOT null,
    status varchar(10)
);

-- Tabla Analysis
CREATE TABLE IF NOT EXISTS Analysis(
    id_analysis INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    imput_image_path varchar(255) NOT NULL,
    timestamp datetime,
    status varchar(15),
    processing_time datetime,
    source varchar(255)
);

-- Tabla Items
CREATE TABLE IF NOT EXISTS Item(
    id_item INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    item_tag_id int not null,
    name varchar(30) not null,
    description TEXT NOT NULL
);

-- Tabla ItemTags
CREATE TABLE IF NOT EXISTS ItemTag(
    id_tag INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    tag_name VARCHAR(30) NOT NULL
);
