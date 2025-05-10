-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS desarrollov_app;
USE desarrollov_app;

-- Tabla Session
CREATE TABLE IF NOT EXISTS Session(
    id_session INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name_session VARCHAR(20) NOT NULL
);

-- Tabla MediaContent
CREATE TABLE IF NOT EXISTS MediaContent(
    id_media INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    session_id INT NOT NULL,
    route_path VARCHAR(64) NOT NULL,
    type_content VARCHAR(30) NOT NULL,
    description VARCHAR(50),
    date_uploaded DATETIME NOT NULL
);

-- Tabla AnalysisResult
CREATE TABLE IF NOT EXISTS AnalysisResult(
    id_results INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    media_id INT NOT NULL,
    detected_labels VARCHAR(50) NOT NULL,
    date_analysis DATETIME NOT NULL
);

-- Tabla QueryHistory
CREATE TABLE IF NOT EXISTS QueryHistory(
    id_query INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    media_id INT NOT NULL,
    date_consultation DATETIME NOT NULL,
    counter INT NOT NULL DEFAULT 1
);

-- Tabla Items
CREATE TABLE IF NOT EXISTS Items(
    id_items INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    media_id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    description TEXT NOT NULL
);

-- Tabla ItemTags
CREATE TABLE IF NOT EXISTS ItemTags(
    id_tag INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    items_id INT NOT NULL,
    tag_name VARCHAR(30) NOT NULL
);
