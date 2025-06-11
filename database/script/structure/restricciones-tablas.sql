-- Evita duplicidad de nombres de tags
ALTER TABLE ItemTag
ADD CONSTRAINT uq_itemtag_tag_name UNIQUE (tag_name);

-- Evita que un mismo nombre de ítem se repita dentro de la misma categoría/tag
ALTER TABLE Item
ADD CONSTRAINT uq_item_name_per_tag UNIQUE (item_tag_id, name);

-- Evita que se repita la ruta de un archivo multimedia para un mismo ítem
ALTER TABLE MediaContent
ADD CONSTRAINT uq_media_route_per_item UNIQUE (item_id, route_path);

-- Evita que se repita el análisis para el mismo ítem y la misma fecha
ALTER TABLE AnalysisResult
ADD CONSTRAINT uq_analysisresult_item_date UNIQUE (item_id, date_analysis);

-- Evita que se repita la ruta de imagen de entrada en análisis
ALTER TABLE Analysis
ADD CONSTRAINT uq_analysis_input_image_path UNIQUE (imput_image_path);

-- Evita que se repita el análisis para el mismo ítem y análisis
ALTER TABLE AnalysisResult
ADD CONSTRAINT uq_analysisresult_item_analysis UNIQUE (item_id, analysis_id);