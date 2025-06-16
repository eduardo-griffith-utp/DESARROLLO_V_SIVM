USE desarrollov_app;

-- Añadiendo las claves foráneas a las tabla MediaContent -> Item
-- Si se elimina un ItemTag, se eliminan automáticamente los Item asociados
-- Si se elimina un Item, se eliminan automáticamente los MediaContent asociados
ALTER TABLE MediaContent  
ADD CONSTRAINT fk_mediacontent_item
FOREIGN KEY (item_id) REFERENCES Item(id_item)
ON DELETE CASCADE;

-- Añadiendo las claves foráneas a las tabla Item -> ItemTag
-- Si se elimina un ItemTag, se eliminan automáticamente los Item asociados
ALTER TABLE Item
ADD CONSTRAINT fk_item_item_tag
FOREIGN KEY (item_tag_id) REFERENCES ItemTag(id_tag)
ON DELETE CASCADE;

-- Añadiendo las claves foráneas a las tabla AnalysisResult -> Item
-- Si se elimina un Item, se eliminan automáticamente los AnalysisResult asociados
ALTER TABLE AnalysisResult 
ADD CONSTRAINT fk_analysisresult_item
FOREIGN KEY (item_id) REFERENCES Item(id_item)
ON DELETE CASCADE;

-- Añadiendo las claves foráneas a las tabla AnalysisResult -> Analysis
-- Si se elimina un Analysis, se eliminan automáticamente los AnalysisResult asociados
ALTER TABLE AnalysisResult  
ADD CONSTRAINT fk_analysisresult_analysis
FOREIGN KEY (analysis_id) REFERENCES Analysis(id_analysis)
ON DELETE CASCADE;