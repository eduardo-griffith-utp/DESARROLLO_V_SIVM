alter table mediacontent 
add constraint fk_mediacontent_session
foreign key (user_id) references Session(id_session); 

alter table analysisresult  
add constraint fk_analisysresults_mediacontent
foreign key (media_is) references MediaContent(id_media); 

alter table queryhistory  
add constraint fk_queryhistory_mediacontent
foreign key (media_id) references MediaContent(id_media) ;

alter table items 
add constraint fk_items_mediacontent
foreign key (media_id) references MediaContent(id_media);

alter table ItemTags 
add constraint fk_itemtags_items
foreign key (item_id) references items(id_items) ;
