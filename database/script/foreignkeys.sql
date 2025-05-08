-- Llaves foráneas corregidas
/*ALTER TABLE MediaContent 
ADD CONSTRAINT fk_mediacontent_session
FOREIGN KEY (session_id) REFERENCES Session(id_session);

ALTER TABLE AnalysisResult  
ADD CONSTRAINT fk_analysisresult_mediacontent
FOREIGN KEY (media_id) REFERENCES MediaContent(id_media);

ALTER TABLE QueryHistory  
ADD CONSTRAINT fk_queryhistory_mediacontent
FOREIGN KEY (media_id) REFERENCES MediaContent(id_media);

ALTER TABLE Items 
ADD CONSTRAINT fk_items_mediacontent
FOREIGN KEY (media_id) REFERENCES MediaContent(id_media);

ALTER TABLE ItemTags 
ADD CONSTRAINT fk_itemtags_items
FOREIGN KEY (items_id) REFERENCES Items(id_items);
*/

ALTER TABLE MediaContent  
ADD CONSTRAINT fk_mediacontent_item
FOREIGN KEY (item_id) REFERENCES Item(id_item);

ALTER TABLE item  
ADD CONSTRAINT fk_mediacontent_item_tag
FOREIGN KEY (item_tag_id) REFERENCES item_tag(id_tag);

