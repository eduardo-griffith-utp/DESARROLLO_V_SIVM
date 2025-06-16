USE desarrollov_app;

-- Orden correcto: primero las más dependientes, luego las raíces
DROP TABLE IF EXISTS AnalysisResult;
DROP TABLE IF EXISTS MediaContent;
DROP TABLE IF EXISTS Analysis;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS ItemTag;