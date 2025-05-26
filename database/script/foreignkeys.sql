ALTER TABLE MediaContent  
ADD CONSTRAINT fk_mediacontent_item
FOREIGN KEY (item_id) REFERENCES Item(id_item);

ALTER TABLE item
ADD CONSTRAINT fk_item_item_tag
FOREIGN KEY (item_tag_id) REFERENCES itemtag(id_tag);

ALTER TABLE analysisresult 
ADD CONSTRAINT fk_analysisresult_item
FOREIGN KEY (item_id) REFERENCES item(id_item);

ALTER TABLE analysisresult  
ADD CONSTRAINT fk_analysisresult_analysis
FOREIGN KEY (analysis_id) REFERENCES analysis(id_analysis);

