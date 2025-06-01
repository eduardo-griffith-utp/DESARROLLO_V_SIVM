--------------------------------------------------------------
select * 
from item_tag as it
    inner join item as i on i.item_tag = it.id_tag
where 
    tag_name like '%' ;

--------------------------------------------------------------
select * 
from item as i 
    inner join MediaContent as mc on mc.item_id = i.
where 
    mc.description like '%'; 

--------------------------------------------------------------
select * 
from item as i
    inner join AnalysisResult as ar on ar.item_id = i.id_item
where 
    ar.date_analysis = 'timestamp a buscar'; 
    --aqui reemplazar por el timestamp obtenido durante la ejecución

--------------------------------------------------------------
select * 
from AnalysisResult as ar
    inner join Analysis as a on a.id_analysis = ar.analysis_id
where 
    a.timestamp = 'timestamp a buscar'