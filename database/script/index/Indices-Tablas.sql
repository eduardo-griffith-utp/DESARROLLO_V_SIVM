-- =======================
-- INDICES PARA LA TABLA Item
-- =======================

-- DROP
DROP INDEX IF EXISTS idx_item_tag_id ON Item;
DROP INDEX IF EXISTS ft_item_name_description ON Item;
DROP INDEX IF EXISTS ft_item_name ON Item;
DROP INDEX IF EXISTS ft_item_description ON Item;

-- CREATE
CREATE INDEX idx_item_tag_id ON Item (item_tag_id);
CREATE FULLTEXT INDEX ft_item_name ON Item (name);
CREATE FULLTEXT INDEX ft_item_description ON Item (description);

-- =======================
-- INDICES PARA LA TABLA ItemTag
-- =======================

-- DROP
DROP INDEX IF EXISTS idx_tag_name ON ItemTag;

-- CREATE
CREATE UNIQUE INDEX idx_tag_name ON ItemTag (tag_name);

-- =======================
-- INDICES PARA LA TABLA MediaContent
-- =======================

-- DROP
DROP INDEX IF EXISTS idx_media_item_id ON MediaContent;
DROP INDEX IF EXISTS idx_media_date_type ON MediaContent;
DROP INDEX IF EXISTS idx_media_date_uploaded ON MediaContent;
DROP INDEX IF EXISTS idx_media_type ON MediaContent;

-- CREATE
CREATE INDEX idx_media_item_id ON MediaContent (item_id);
CREATE INDEX idx_media_date_uploaded ON MediaContent (date_uploaded);
CREATE INDEX idx_media_type ON MediaContent (type);

-- =======================
-- INDICES PARA LA TABLA Analysis
-- =======================

-- DROP
DROP INDEX IF EXISTS idx_analysis_timestamp ON Analysis;
DROP INDEX IF EXISTS ft_analysis_input_image_path ON Analysis;

-- CREATE
CREATE INDEX idx_analysis_timestamp ON Analysis (timestamp);
CREATE FULLTEXT INDEX ft_analysis_input_image_path ON Analysis (input_image_path);

-- =======================
-- INDICES PARA LA TABLA AnalysisResult
-- =======================

-- DROP
DROP INDEX IF EXISTS idx_result_item_id ON AnalysisResult;
DROP INDEX IF EXISTS idx_result_analysis_id ON AnalysisResult;
DROP INDEX IF EXISTS idx_result_date_status ON AnalysisResult;
DROP INDEX IF EXISTS idx_result_date_analysis ON AnalysisResult;
DROP INDEX IF EXISTS idx_result_status ON AnalysisResult;
DROP INDEX IF EXISTS ft_detected_labels ON AnalysisResult;

-- CREATE
CREATE INDEX idx_result_item_id ON AnalysisResult (item_id);
CREATE INDEX idx_result_analysis_id ON AnalysisResult (analysis_id);
CREATE INDEX idx_result_date_analysis ON AnalysisResult (date_analysis);
CREATE INDEX idx_result_status ON AnalysisResult (status);
CREATE FULLTEXT INDEX ft_detected_labels ON AnalysisResult (detected_labels);